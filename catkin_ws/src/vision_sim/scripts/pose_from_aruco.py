#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import CompressedImage
from geometry_msgs.msg import Twist, Vector3
import cv2
from cv_bridge import CvBridge
import numpy as np


ARUCO_DICT = {
	"DICT_4X4_50": cv2.aruco.DICT_4X4_50,
	"DICT_4X4_100": cv2.aruco.DICT_4X4_100,
	"DICT_4X4_250": cv2.aruco.DICT_4X4_250,
	"DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
	"DICT_5X5_50": cv2.aruco.DICT_5X5_50,
	"DICT_5X5_100": cv2.aruco.DICT_5X5_100,
	"DICT_5X5_250": cv2.aruco.DICT_5X5_250,
	"DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
	"DICT_6X6_50": cv2.aruco.DICT_6X6_50,
	"DICT_6X6_100": cv2.aruco.DICT_6X6_100,
	"DICT_6X6_250": cv2.aruco.DICT_6X6_250,
	"DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
	"DICT_7X7_50": cv2.aruco.DICT_7X7_50,
	"DICT_7X7_100": cv2.aruco.DICT_7X7_100,
	"DICT_7X7_250": cv2.aruco.DICT_7X7_250,
	"DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
	"DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
	"DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
	"DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
	"DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
	"DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
}

def pose_estimation(frame, matrix_coefficients, distortion_coefficients):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
    aruco_params = cv2.aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray,
        aruco_dict,
        parameters=aruco_params,
        cameraMatrix=matrix_coefficients,
        distCoeff=distortion_coefficients)

    if len(corners) > 0:
        for i in range(0, len(ids)):
           
            rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners[i], 0.02, matrix_coefficients,
                                                                       distortion_coefficients)
            
            cv2.aruco.drawDetectedMarkers(frame, corners) 

            cv2.aruco.drawAxis(frame, matrix_coefficients, distortion_coefficients, rvec, tvec, 0.01)  

    return frame


def image_callback(msg):
    # # Obtener la última imagen del nodo de ROS
    # imagen = rospy.wait_for_message("/blue_rov1/CompressedImage", CompressedImage)
	
    # # Procesar la imagen y hacer una predicción
    # np_arr = np.frombuffer(imagen.data, np.uint8)
    # cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    # #cv_image= cv_image[0:128,450:640]

    # Convert ROS message to OpenCV image
    cv_image = bridge.compressed_imgmsg_to_cv2(msg)
    
    gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    
    h,w,_ = cv_image.shape

    width = 1200
    height = int(width*(h/w))
    img = cv2.resize(cv_image, (width, height), interpolation=cv2.INTER_CUBIC)


    # Detect ArUco markers in the image
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(img, aruco_dict, parameters=aruco_params)
    
    img_markers = cv2.aruco.drawDetectedMarkers(img, corners, ids)
    output = pose_estimation(img, intrinsic_camera, distortion)

    # cv2.imshow("Imagen", cv_image)
    # cv2.imshow("resized img", img)
    cv2.imshow('Estimated Pose', output)
    cv2.waitKey(1)
    

    print(ids)
    if ids is None:
            return
    
    
    # Publica un mensaje en el tópico de velocidad de Twist en función de la clasificación
    twist_msg = Twist()
    moverobot=0
    if moverobot == 1:
        twist_msg.linear.x = 0.01
        twist_msg.angular.z = 10.0
    else:
        twist_msg.linear.x = 0.0
        twist_msg.angular.z = 0.0
    twist_pub.publish(twist_msg)
    
    
if __name__ == '__main__':
    # Initialize ROS node
    rospy.init_node('aruco_detection')
    rospy.loginfo("node started")

    # Initialize image bridge
    bridge = CvBridge()

    intrinsic_camera = np.array(((933.15867, 0, 657.59),(0,933.1586, 400.36993),(0,0,1)))
    distortion = np.array((-0.43948,0.18514,0,0))

    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
    aruco_params = cv2.aruco.DetectorParameters_create()

    
    
    # Adjust detector parameters for underwater images
    # aruco_params.adaptiveThreshConstant = 5
    # aruco_params.minMarkerPerimeterRate = 0.03
    # aruco_params.maxMarkerPerimeterRate = 4.0
    # aruco_params.polygonalApproxAccuracyRate = 0.05
    # aruco_params.minCornerDistanceRate = 0.05

    # Initialize previous marker id and transformation matrix
    prev_marker_id = None
    prev_marker_transform = None

    # Subscribe to the camera image topic
    image_sub = rospy.Subscriber('/blue_rov1/CompressedImage', CompressedImage, image_callback)

    # Publish to the Twist topic
    twist_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    rospy.spin()
    
    
    
