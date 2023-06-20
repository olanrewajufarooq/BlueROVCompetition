#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import CompressedImage
from geometry_msgs.msg import Twist, Vector3
import cv2
from cv_bridge import CvBridge
import numpy as np
import torch
import matplotlib.pyplot as plt
model = torch.hub.load('ultralytics/yolov5','custom',path='/home/haleem/catkin_ws/src/vision_sim/scripts/best.pt',_verbose=False)

def image_callback(msg):
    # Convert ROS message to OpenCV image
    cv_image = bridge.compressed_imgmsg_to_cv2(msg)
    
    rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    # rgb_image = Image.open(cv_image)

    # Object detection using Yolov5
    # cv2.imwrite('test.jpeg',cv_image)
    results = model(rgb_image,size=416)
    # results.show()
    print(results)

    output = results.xyxy
    for obj in output:
        xmin, ymin, xmax, ymax, confidence, class_id = obj[0]
        xmin, ymin, xmax, ymax,class_id = int(xmin),int(ymin),int(xmax),int(ymax), int(class_id)
        # print(f'xmin: {xmin}, ymin: {ymin}, xmax: {xmax}, ymax: {ymax}, confidence: {confidence}, class_id: {class_id}')
        cv2.rectangle(cv_image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
        cv2.putText(cv_image, f'{results.names[class_id]} : {confidence:.2f}', (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the image with the bounding boxes
    cv2.imshow('YOLOv5 Results', cv_image)
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
    
    
    
