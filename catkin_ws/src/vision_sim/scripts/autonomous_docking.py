#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import CompressedImage
from geometry_msgs.msg import Twist, Vector3
import cv2
from cv_bridge import CvBridge
import numpy as np
#import torch
import matplotlib.pyplot as plt
#model = torch.hub.load('ultralytics/yolov5','custom',path='/home/yokko/catkin_ws/src/vision/scripts/best.pt',_verbose=False)

intrinsic_camera = np.array(((1000, 0, 480/2),(0,1000, 640/2),(0,0,1)))
distortion = np.array((0.,0,0,0))


def pose_estimation(frame, matrix_coefficients, distortion_coefficients):
    pose = {}
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

            # Draw ID on the frame
            marker_id = str(ids[i][0])
            marker_center = tuple(np.mean(corners[i][0], axis=0).astype(int))
            cv2.putText(frame, marker_id, marker_center, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            pose[ids[i][0]]= (rvec.squeeze(),tvec.squeeze())
            print(f"id = {ids[i][0]}")
            print(f"rvec = {rvec}")
            print(f"tvec = {tvec}")
            # print(markerPoints)
            cv2.aruco.drawDetectedMarkers(frame, corners) 

            cv2.aruco.drawAxis(frame, matrix_coefficients, distortion_coefficients, rvec, tvec, 0.01)
    return frame,pose


def image_callback(msg):

    cv_image = bridge.compressed_imgmsg_to_cv2(msg)
    
    gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    # h,w,_ = cv_image.shape

    frame,pose = pose_estimation(cv_image, intrinsic_camera, distortion)

    key_list = pose.keys()
    print(key_list)
    cv2.imshow('Estimated Pose', frame)
    cv2.imshow('object detection', cv_image)
    cv2.waitKey(1)


if __name__ == '__main__':
    # Initialize ROS node
    rospy.init_node('obeject_detection')
    rospy.loginfo("node started")
    
    # Initialize image bridge
    bridge = CvBridge()

    # Subscribe to the camera image topic
    image_sub = rospy.Subscriber('/camera0/image_raw/compressed', CompressedImage, image_callback)

    # Publish to the Twist topic
    twist_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rospy.spin()
    