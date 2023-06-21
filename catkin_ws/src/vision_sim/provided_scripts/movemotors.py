#!/usr/bin/python
import rospy
import sys
import argparse

from mavros_msgs.srv import CommandBool, ParamSet, ParamGet
from mavros_msgs.msg import ManualControl, ParamValue, ActuatorControl

G_ROV_ARM_SERVICE_NAME          = '/mavros/cmd/arming'
G_ROV_PARAM_GET_SERVICE_NAME    = '/mavros/param/get'
G_ROV_PARAM_SET_SERVICE_NAME    = '/mavros/param/set'
G_ROV_MANUAL_CONTROL_TOPIC_NAME = '/mavros/manual_control/send'
G_ROV_ACTUATOR_CONTROL_TOPIC_NAME = '/mavros/actuator_control'


G_ROV_LIGHT_AUX_CHANNEL = 7
G_ROV_SERVO_AUX_CHANNEL = 6
G_ROV_DEFAULT_SPEED = 500.0

manual_control = ManualControl()
manual_control.x = 400

pwm_value=0
pwm_port= G_ROV_LIGHT_AUX_CHANNEL

 
def talker(args):
    man_pub = rospy.Publisher(G_ROV_ACTUATOR_CONTROL_TOPIC_NAME, ActuatorControl, queue_size=10)
    rospy.init_node('moveactuators', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        man_pub.publish(args)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        talker(manual_control)
    except rospy.ROSInterruptException:
        pass
