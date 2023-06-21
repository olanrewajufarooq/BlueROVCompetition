import cv2
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
        

    # Reconstruye la imagen a partir de los segmentos recibidos
    image_data = b''.join([segment_data for _, segment_data in received_segments])
    image_array = np.frombuffer(image_data, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    # Muestra la imagen
    try:
        cv2.imshow('Imagen recibida', image)
    except:
        pass
    
    cv2.waitKey(1)

   

# Dirección IP y puerto para recibir la imagen
ip_receptor = '192.168.1.100'
puerto_receptor = 1234

# Recibir la imagen por UDP
while True:
	recibir_imagen(ip_receptor, puerto_receptor)
udp_socket.close()
cv2.destroyAllWindows()
