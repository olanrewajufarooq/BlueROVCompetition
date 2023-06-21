import rospy
from sensor_msgs.msg import CompressedImage
import cv2
from cv_bridge import CvBridge
import numpy as np
    
def procesar_imagen_throttled(event):
    # Obtener la última imagen del nodo de ROS
    imagen = rospy.wait_for_message("/compressedImage", CompressedImage)  #bluerov
	
    # Procesar la imagen y hacer una predicción
    np_arr = np.frombuffer(imagen.data, np.uint8)
    cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    #cv_image= cv_image[0:128,450:640]
    #cv2.imwrite('prediccion',cv_image)
    cv2.imshow("Imagen", cv_image)
    cv2.waitKey(1)
    

    
if __name__ == '__main__':
    # Inicia el nodo de ROS
    rospy.init_node('image_subscriber')
    
    
    intervalo_de_tiempo = rospy.Duration.from_sec(.01)
    rospy.Timer(intervalo_de_tiempo, procesar_imagen_throttled)
    
    rospy.spin()
    
    
    
