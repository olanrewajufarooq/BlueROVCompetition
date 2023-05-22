#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import CompressedImage
from geometry_msgs.msg import Twist, Vector3
import cv2
from cv_bridge import CvBridge
import numpy as np
import torch

model = torch.hub.load('ultralytics/yolov5','custom',path='/home/haleem/catkin_ws/src/vision_sim/scripts/best.pt',_verbose=False)

def image_callback(msg):
    # Convert ROS message to OpenCV image
    cv_image = bridge.compressed_imgmsg_to_cv2(msg)
    # Object detection using Yolov5
    result = model(cv_image)
    cv2.imshow('Object detection', result)
    
    cv2.waitKey(1)
    
if __name__ == '__main__':
    # Initialize ROS node
    rospy.init_node('obeject_detection')
    rospy.loginfo("node started")

    # Initialize image bridge
    bridge = CvBridge()

    # Subscribe to the camera image topic
    image_sub = rospy.Subscriber('/blue_rov1/CompressedImage', CompressedImage, image_callback)
    rospy.spin()
    
    
    
