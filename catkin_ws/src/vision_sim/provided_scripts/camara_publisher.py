import cv2
import rospy
from sensor_msgs.msg import CompressedImage
import socket
import struct
import numpy as np

def recibir_imagen(ip, port):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((ip, port))

    segment_size = 1024  # Tamaño máximo del segmento en bytes
    received_segments = []

    while True:
        # Recibe el segmento por UDP
        segment, addr = udp_socket.recvfrom(segment_size + 4)

        segment_num = struct.unpack('!I', segment[:4])[0]
        segment_data = segment[4:]

        # Almacena el segmento recibido
        received_segments.append((segment_num, segment_data))

        # Verifica si se ha recibido el último segmento
        if len(segment_data) < segment_size:
            break

        # Ordena los segmentos en orden numérico
        received_segments.sort(key=lambda x: x[0])
    try:
	    # Reconstruye la imagen a partir de los segmentos recibidos
	    image_data = b''.join([segment_data for _, segment_data in received_segments])
	    image_array = np.frombuffer(image_data, dtype=np.uint8)
	    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

	    # Publica la imagen como CompressedImage en ROS
	    compressed_image = CompressedImage()
	    compressed_image.header.stamp = rospy.Time.now()
	    compressed_image.format = "jpeg"
	    compressed_image.data = np.array(cv2.imencode('.jpg', image)[1]).tostring()
	    pub.publish(compressed_image)
    except:
    	pass

# Dirección IP y puerto para recibir la imagen
ip_receptor = '192.168.1.100'
puerto_receptor = 1234

# Inicializar el nodo de ROS
rospy.init_node('udp_image_receiver')

# Crear el publicador para la imagen comprimida
pub = rospy.Publisher('/compressedImage', CompressedImage, queue_size=10)

# Recibir la imagen por UDP
while not rospy.is_shutdown():
    recibir_imagen(ip_receptor, puerto_receptor)

udp_socket.close()
cv2.destroyAllWindows()

