#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import CompressedImage
from geometry_msgs.msg import Twist, Vector3
import cv2
from cv_bridge import CvBridge
import numpy as np
import torch
import matplotlib.pyplot as plt
model = torch.hub.load('ultralytics/yolov5','custom',path='/home/yokko/catkin_ws/src/vision/scripts/best.pt',_verbose=False)

intrinsic_camera = np.array(((933.15867, 0, 657.59),(0,933.1586, 400.36993),(0,0,1)))
distortion = np.array((-0.43948,0.18514,0,0))

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

def object_detection(cv_image):
    rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    results = model(rgb_image,size=416)
    print(results)
    center_dict = {}
    output = results.xyxy
    for obj in output:
        xmin, ymin, xmax, ymax, confidence, class_id = obj[0]
        xmin, ymin, xmax, ymax,class_id = int(xmin),int(ymin),int(xmax),int(ymax), int(class_id)
        center_x = (xmin + xmax) / 2
        center_y = (ymin + ymax) / 2
        center_dict[class_id] = (center_x,center_y)
        cv2.rectangle(cv_image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
        cv2.putText(cv_image, f'{results.names[class_id]} : {confidence:.2f}', (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    return center_dict
def image_callback(msg):

    cv_image = bridge.compressed_imgmsg_to_cv2(msg)
    
    gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    
    h,w,_ = cv_image.shape

    width = 1200
    height = int(width*(h/w))
    img = cv2.resize(cv_image, (width, height), interpolation=cv2.INTER_CUBIC)

    frame,pose = pose_estimation(img, intrinsic_camera, distortion)

    
    key_list = pose.keys()
    print(key_list)
    if len(key_list) == 0:
        print('---------object detection------')
        center_dict = object_detection(cv_image)
        keys = center_dict.keys()
        if 2 in keys:
            error_y =center_dict[2][0] -  cv_image.shape[0] / 2
            error_z =center_dict[2][1] -  cv_image.shape[1] / 2
            kp_ob = 0.01
            surge_control =  0.5 
            sway_control = kp_ob*error_y
            heave_control = kp_ob*error_z

    else:
        err_x = 0
        err_y = 0
        err_z = 0
        if 100 in key_list:
            kp_surge = 0.5
            curr_x = pose[100][1][2]
            curr_y = pose[100][1][0]
            curr_z = pose[100][1][1]
            des_x = 0.15
            des_y = -0.02
            des_z = 0
            thres = 0.005
            err_x = curr_x - des_x
            err_y = curr_y - des_y
            err_z = curr_z - des_z

            if np.abs(err_x) <= thres:
                err_x = 0
            if np.abs(err_y) <= thres:
                err_y = 0
            if np.abs(err_z) <= thres:
                err_z = 0
        else:
            kp_surge = 0.01
            if 74 in key_list: #BL
                err_x = pose[74][1][2]
                err_y = pose[74][1][0] + 0.09
                err_z = pose[74][1][1]
            elif 75 in key_list: #BR
                err_x = pose[75][1][2]
                err_y = pose[75][1][0] - 0.05
                err_z = pose[75][1][1]
            elif 76 in key_list: #TR
                err_x = pose[76][1][2]
                err_y = pose[76][1][0] - 0.05
                err_z = pose[76][1][1] + 0.05
            elif 77 in key_list: #TL
                err_x = pose[77][1][2]
                err_y = pose[77][1][0] + 0.09
                err_z = pose[77][1][1] + 0.05
        kp = 0.5
        surge_control = kp_surge * err_x 
        sway_control = kp*err_y
        heave_control = kp*err_z
    


    # Publica un mensaje en el tópico de velocidad de Twist en función de la clasificación
    twist_msg = Twist()
    moverobot=1
    if moverobot == 1:
        #negative forward
        twist_msg.linear.x = -surge_control
        #positive right
        twist_msg.linear.y = sway_control
        #negative up
        twist_msg.linear.z = heave_control
    else:
        twist_msg.linear.x = 0.0
        twist_msg.angular.z = 0.0
    twist_pub.publish(twist_msg)
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
    image_sub = rospy.Subscriber('/blue_rov1/CompressedImage', CompressedImage, image_callback)


    # Publish to the Twist topic
    twist_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rospy.spin()
    