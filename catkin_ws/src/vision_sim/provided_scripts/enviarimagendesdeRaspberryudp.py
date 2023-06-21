import cv2
import socket
import struct

def enviar_imagen(ip, port):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Crea el objeto de captura de video
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

    segment_size = 1024  # Tama      o m      ximo del segmento en bytes

    while True:
        # Lee un fotograma del video
        ret, frame = cap.read()

        # Cambia el tama      o del fotograma
        frame = cv2.resize(frame, (800, 600))

        # Codifica el fotograma en formato JPEG
        _, frame_data = cv2.imencode('.jpg', frame)

        # Divide la imagen en segmentos y env      a cada segmento por UDP
        total_size = len(frame_data)
        num_segments = total_size // segment_size + 1

        for i in range(num_segments):
            start = i * segment_size
            end = min((i + 1) * segment_size, total_size)

            segment = frame_data[start:end].tobytes()
            udp_socket.sendto(struct.pack('!I', i) + segment, (ip, port))

        # Espera la pulsaci      n de la tecla 'q' para salir del bucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    udp_socket.close()
    cap.release()
    cv2.destroyAllWindows()

# Direcci      n IP y puerto del destinatario
ip_destinatario = '192.168.2.1'
puerto_destinatario = 1234

# Enviar la imagen por UDP
enviar_imagen(ip_destinatario, puerto_destinatario)

