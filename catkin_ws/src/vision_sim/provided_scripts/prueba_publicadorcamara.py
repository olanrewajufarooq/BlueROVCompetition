import rospy
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
import cv2

def publish_camera():
    # Inicializar el nodo de ROS
    rospy.init_node('camera_publisher', anonymous=True)

    # Crear un publicador para el tópico de imagen comprimida
    image_pub = rospy.Publisher('/prueba', CompressedImage, queue_size=10)

    # Crear un objeto CvBridge
    bridge = CvBridge()

    # Crear el objeto de captura de video
    cap = cv2.VideoCapture(0)

    # Configurar la tasa de publicación en Hz
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        # Leer un fotograma del video
        ret, frame = cap.read()

        # Comprobar si se ha leído correctamente
        if not ret:
            rospy.logwarn("Error al leer el fotograma de la cámara")
            continue

        # Comprimir la imagen utilizando el formato JPEG y una calidad del 80%
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 80]
        _, jpeg_data = cv2.imencode('.jpg', frame, encode_param)

        # Crear el mensaje de imagen comprimida de ROS
        image_msg = CompressedImage()
        image_msg.header.stamp = rospy.Time.now()
        image_msg.format = "jpeg"
        image_msg.data = jpeg_data.tostring()

        # Publicar la imagen comprimida
        image_pub.publish(image_msg)

        # Dormir para mantener la tasa de publicación
        rate.sleep()

    # Liberar los recursos y cerrar la ventana de OpenCV
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        # Llamar a la función para publicar la cámara en el tópico /prueba
        publish_camera()
    except rospy.ROSInterruptException:
        pass

