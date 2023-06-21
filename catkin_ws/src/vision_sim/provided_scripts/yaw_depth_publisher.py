import rospy
from std_msgs.msg import Float32
from pymavlink import mavutil

rospy.init_node('publish_yaw_depth')  # Inicializar el nodo de ROS

# Crear los publicadores para los valores de yaw y profundidad
yaw_pub = rospy.Publisher('yaw', Float32, queue_size=10)
depth_pub = rospy.Publisher('depth', Float32, queue_size=10)

# Establecer la conexión con el vehículo
connection = mavutil.mavlink_connection('udp:192.168.2.1:14770')

while not rospy.is_shutdown():
    msg = connection.recv_match()
    if msg is None:
        continue
    
    # Mensaje de actitud (yaw)
    if msg.get_type() == 'ATTITUDE':
        yaw = msg.yaw * 57.2958
        yaw_pub.publish(yaw)  # Publicar el valor de yaw
    
    # Mensaje de posición global (altitud relativa)
    if msg.get_type() == 'GLOBAL_POSITION_INT':
        relative_altitude = (msg.relative_alt +65)*1.5 / 1000.0  # Convertir a metros
        depth_pub.publish(relative_altitude)  # Publicar el valor de profundidad relativa

    
    rospy.sleep(0.01)  # Esperar un breve tiempo

# Finalizar el nodo de ROS
rospy.spin()

