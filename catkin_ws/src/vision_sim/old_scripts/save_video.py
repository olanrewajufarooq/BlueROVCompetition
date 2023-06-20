#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import CompressedImage
from geometry_msgs.msg import Twist, Vector3
import cv2
from cv_bridge import CvBridge
import numpy as np

video_file = "./output_video.avi" # Save the video file in the current directory
fourcc = cv2.VideoWriter_fourcc(*'MJPG')# Specify the codec (fourcc) for the video file
fps = 20.0  # Specify the frames per second for the video
width, height = 640, 480  # Specify the desired width and height for the video

# Create a video writer object
video_writer = cv2.VideoWriter(video_file, fourcc, fps, (width, height))


def image_callback(msg):
    
    try:
        # Convert ROS image message to OpenCV format
        cv_image = bridge.compressed_imgmsg_to_cv2(msg)

        # Write the image frame to the video file
        video_writer.write(cv_image)

        # Display the image frame (optional)
        cv2.imshow("Image", cv_image)
        cv2.waitKey(1)
    except Exception as e:
        rospy.logerr(e)
    
    
if __name__ == '__main__':
    
    # Initialize ROS node
    rospy.init_node('save_video')
    rospy.loginfo("node started")

    # Initialize image bridge
    bridge = CvBridge()

    # Subscribe to the camera image topic
    image_sub = rospy.Subscriber('/blue_rov1/CompressedImage', CompressedImage, image_callback)

    rospy.spin()
    
    
    
