#!/usr/bin/env python3
import rospy
from mavros_msgs.msg import OverrideRCIn
from mavros_msgs.msg import RCOut

"""
Cmd_velocity subscriber for the bluerov, the script takes the velocities values and compute the PWM velocity of the motors
The udp direction have to be eddited in this script and in the end point settings form the BlueOS
"""
from geometry_msgs.msg import Twist
import numpy as np
from std_msgs.msg import Int32
import time
#----------------inicializacion del servo--------------------------------------------------
servvelant=1500
#-------------------------coeficientes de la caracterizacion de la velocidad-----------------------------
a = 1.3871668161975536e-25
b = -2.080750463000313e-21
c = 1.3983334487807407e-17
d = -5.543948233018681e-14
e = 1.4359451930265564e-10
f = -2.5387836010458446e-07
g = 0.0003102899349247361
h = -0.25886076958834003
i = 141.07497402237286
j = -45353.82880615414
k = 6531725.54047377
coefficients = np.array([a, b, c, d, e, f, g, h,i,j, k])

# Generar arreglo de x desde 1100 hasta 1900
x = np.linspace(1100, 1900, 801)

# Calcular los valores de y ajustados
y = np.polyval(coefficients, x)

velocidades= np.zeros(801)
# crear arreglo de la re
z=0
for i in range(len(x)):
    if (z<400):
      velocidades[z]=-y[i]
    else: 
      velocidades[z]=y[i]
#---------------------------Zona muerta de los motores----------------------------  
    #if (z>390 and z<410):
    #  velocidades[z]=0.0
    z=z+1
    

def callback(data):
    # Acciones a realizar cuando se recibe un mensaje en el tópico
    rospy.loginfo("Velocidad lineal: %s", data.linear)
    rospy.loginfo("Velocidad angular: %s", data.angular)
    channels=[1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1100, 1100, 0, 0, 0, 0, 0, 0, 0, 0]
#------------------------------linear x-------------------------    
    if data.linear.x>=-1.0 and data.linear.x<=1.0 and data.linear.x!=0.0:
    	diff = np.abs(velocidades - data.linear.x)
    	xpwm = np.argmin(diff)+1100
    	channels[4]=xpwm
    	print("Publishing x pwm: ", xpwm)
    else:
    	channels[4]=1500
    	
#------------------------------linear y-------------------------    
    if data.linear.y>=-1.0 and data.linear.y<=1.0 and data.linear.y!=0.0:
    	diff = np.abs(velocidades - data.linear.y)
    	ypwm = np.argmin(diff)+1100
    	channels[5]=ypwm
    	print("Publishing y pwm: ", ypwm)
    else:
    	channels[5]=1500
    	
#------------------------------linear z-------------------------    
    if data.linear.z>=-1.0 and data.linear.z<=1.0 and data.linear.z!=0.0:
    	diff = np.abs(velocidades - data.linear.z)
    	zpwm = np.argmin(diff)+1100
    	channels[2]=zpwm
    	print("Publishing z pwm: ", zpwm)
    else:
    	channels[2]=1500
    	
#------------------------------angular z-------------------------    
    if data.angular.z>=-1.0 and data.angular.z<=1.0 and data.angular.z!=0.0:
    	diff = np.abs(velocidades - data.angular.z)
    	yawpwm = np.argmin(diff)+1100
    	channels[3]=yawpwm
    	print("Publishing yaw pwm: ", yawpwm)
    else:
    	channels[3]=1500
    pub.publish(channels)

def callback_camara_servo(data):
    # Acciones a realizar cuando se recibe un mensaje en el tópico 'camara_servo'
    global servvelant
    rospy.loginfo("reading camara_servo topic: %s", data.data)
    #------------------------------Servo camara-------------------------    
    if data.data>=-1100 and data.data<=1900 and servvelant!=data.data:
    	set_rc_channel_pwm(8, data.data)
    	print("Publishing camera servo pwm: ", 1600)
    	time.sleep(3)
    	servvelant=data.data
    	set_rc_channel_pwm(8, 1500)
    	
    else:
    	set_rc_channel_pwm(8, 1500)
	
    pub.publish(channels)


def listener():
    rospy.init_node('cmd_vel_subscriber', anonymous=True)
    print("Ros node created")
    # Se suscribe al tópico 'cmd_vel' con el mensaje de tipo Twist
    rospy.Subscriber('cmd_vel', Twist, callback)
    rospy.Subscriber('camara_servo', Int32, callback_camara_servo)
    

    # Mantiene el programa en funcionamiento hasta que se reciba una señal de interrupción (Ctrl+C)
    rospy.spin()

if __name__ == '__main__':
   pub = rospy.Publisher('/mavros/rc/override', OverrideRCIn, queue_size=10)
   listener()

