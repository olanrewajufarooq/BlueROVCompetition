##!/usr/bin/python

from geometry_msgs.msg import TwistStamped
import termios, fcntl, sys, os
import rospy
import urlparse
import time

#import service library
from std_srvs.srv import Empty

import math
#from cola2_msgs.msg import NavSts, BodyVelocityReq, GoalDescriptor
from pymavlink import mavutil

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

# Instantiate CvBridge
bridge = CvBridge()
cv2_img = Image
PORT_NUMBER = 8088
HOST_NAME = 'localhost'

def image_callback(msg):
    global cv2_img
    #print("Received an image!")
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
	#print("image_callback:Image Received")
    except CvBridgeError, e:
        print(e)
    #else:
        # Save your OpenCV2 image as a jpeg 
        #cv2.imwrite('camera_image.jpeg', cv2_img)


#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	baseVelocity=0.5
    	#Define your image topic
    	image_topic = "/camera/image_raw"
    	# Set up your subscriber and define its callback
	rospy.Subscriber(image_topic, Image, image_callback)
	#pub = rospy.Publisher("controller/body_velocity_req",BodyVelocityReq,queue_size=1)
	rospy.init_node('CRFSS_Proxy_ROS_Camera')
	print("MyHandler __init__")
	
	#Handler for the GET requests
	def do_GET(self):
		global cv2_img
		print("do_Get")

		# Save your OpenCV2 image as a jpeg 
		#cv2.imwrite('camera_image.jpeg', cv2_img)
	
		self.send_response(200)
		#self.send_header('Content-type','text/html')
		self.send_header('Content-type','image/jpeg')
		encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]
		result, encimg = cv2.imencode('.jpg', cv2_img, encode_param)
		if False==result:
		    print 'could not encode image!'
		    quit()

		img_length = len(encimg)
		#print(img_length)
		self.send_header('Content-Length',img_length)
		self.end_headers()
		# Send the html message
		#self.wfile.write("Hello World !")
		#jpeg_image = cv2.EncodeImage('.jpg', cv2_img)

		img_bytes = encimg.tobytes()
		self.wfile.write(img_bytes)
		#rospy.sleep(0.1)
		return


if __name__ == '__main__':

    server = HTTPServer((HOST_NAME, PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER
    
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
