#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import CompressedImage
from geometry_msgs.msg import Twist, Vector3
import cv2
from cv_bridge import CvBridge
import numpy as np

def procesar_imagen_throttled(event):
    # Obtener la última imagen del nodo de ROS
    imagen = rospy.wait_for_message("/blue_rov1/CompressedImage", CompressedImage)
	
    # Procesar la imagen y hacer una predicción
    np_arr = np.frombuffer(imagen.data, np.uint8)
    cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    #cv_image= cv_image[0:128,450:640]

    gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    # Detect ArUco markers in the image
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray_image, aruco_dict, parameters=aruco_params)
    
    img_markers = cv2.aruco.drawDetectedMarkers(cv_image, corners, ids)
    cv2.imshow("Imagen", cv_image)
    cv2.imshow("gray", gray_image)
    cv2.waitKey(1)
    

    print(ids)
    if ids is None:
            return
    cv2.imshow("Imagen", cv_image)
    cv2.waitKey(1)
    
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
    # Inicia el nodo de ROS
    rospy.init_node('image_classifier')
    
    # Define marker dictionary and parameters
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
    aruco_params = cv2.aruco.DetectorParameters_create()
    intervalo_de_tiempo = rospy.Duration.from_sec(1)
    rospy.Timer(intervalo_de_tiempo, procesar_imagen_throttled)
    

    # Publica en el tópico de Twist
    twist_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.spin()
    
    
    
