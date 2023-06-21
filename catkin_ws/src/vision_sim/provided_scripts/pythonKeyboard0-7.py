"""
Example of how to Arm and Disarm an Autopilot with pymavlink
"""
# Import mavutil
from pymavlink import mavutil
import keyboard as key
import time as time

# Create the connection
#master = mavutil.mavlink_connection('udpin:192.168.2.1:14550')
master = mavutil.mavlink_connection('udpin:127.0.0.1:14551')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

ex = False
kpress = False
x = 0
y = 0
z = 0
rotation = 0
speed = 1600
armed = False

# https://mavlink.io/en/messages/common.html#MAV_CMD_COMPONENT_ARM_DISARM
"""hjhjjhhj
# Arm
# master.arducopter_arm() or:
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0)

# Disarm
# master.arducopter_disarm() or:
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    0, 0, 0, 0, 0, 0, 0)"""


#Inputs por teclado
while(ex==False):
    kpress=False

    #Depth
    if(key.is_pressed('q') and z != 1000): 
        z = 1000
        kpress=True
    elif(key.is_pressed('e') and z != 0): 
        z = 0
        kpress=True
    else:
        z = 500

    #Forward/Backward
    if(key.is_pressed('w') and x != speed): 
        x = speed
        kpress=True
    elif(key.is_pressed('s') and x != -speed): 
        x = -speed
        kpress=True
    else:
        x = 0

    #Right/Left
    if(key.is_pressed('a') and y != -speed): 
        y = -speed
        kpress=True
    elif(key.is_pressed('d') and y != speed): 
        y = speed
        kpress=True
    else:
        y = 0

    #Rotation
    if(key.is_pressed('x') and rotation != speed): 
        rotation = speed
        kpress=True
    elif(key.is_pressed('z') and rotation != -speed): 
        rotation = -speed
        kpress=True
    else:
        rotation = 0


    #ARM DISARM
    if(key.is_pressed('m')):
        if(armed):
            armed = False
            master.mav.command_long_send(
                master.target_system,
                master.target_component,
                mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                0,
                0, 0, 0, 0, 0, 0, 0)
	    time.sleep(0.1)
        else:
            armed = True
            master.mav.command_long_send(
                master.target_system,
                master.target_component,
                mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                0,
                1, 0, 0, 0, 0, 0, 0)
	    time.sleep(0.1)

    #LIGHTS OFF
    if(key.is_pressed('l')):
        '''master.mav.command_long_send(
                master.target_system,
                master.target_component,
                mavutil.mavlink.MAV_CMD_ILLUMINATOR_ON_OFF,
                0,
                0, 0, 0, 0, 0, 0, 0)'''
    	master.mav.manual_control_send(
        	master.target_system,
        	x, #x
        	y, #y
        	z, #z
        	rotation, #rotation
        	1<<13) #active button
        time.sleep(0.1)
    #LIGHTS ON
    if(key.is_pressed('k')):
            #illumOn = True
            '''master.mav.command_long_send(
                master.target_system,
                master.target_component,
                mavutil.mavlink.MAV_CMD_ILLUMINATOR_ON_OFF,
                0,
                1, 0, 0, 0, 0, 0, 0)'''
            master.mav.manual_control_send(
                master.target_system,
                x, #x
                y, #y
                z, #z
                rotation, #rotation
                1<<14) #active button
	    time.sleep(0.1)

    #GRIPPER 
    #CLOSE
    if(key.is_pressed('h')):
        '''master.mav.command_long_send(
                master.target_system,
                master.target_component,
                mavutil.mavlink.MAV_CMD_DO_GRIPPER,
                0,
                1, 1, 0, 0, 0, 0, 0)'''
        master.mav.manual_control_send(
            master.target_system,
            x, #x
            y, #y
            z, #z
            rotation, #rotation
            1<<9) #active button
    #OPEN
    elif(key.is_pressed('j')):
        '''master.mav.command_long_send(
                master.target_system,
                master.target_component,
                mavutil.mavlink.MAV_CMD_DO_GRIPPER,
                0,
                1, 0, 0, 0, 0, 0, 0)'''
        master.mav.manual_control_send(
            master.target_system,
            x, #x
            y, #y
            z, #z
            rotation, #rotation
            1<<10) #active button


    #exit
    if(key.is_pressed('o')):
        x = 0
        y= 0
        z = 500
        rotation = 0
        ex = True

    #signal
    if(kpress==True):
        kpress=False
        master.mav.manual_control_send(
            master.target_system,
            x, #x
            y, #y
            z, #z
            rotation, #rotation
            0) #active button
        print("signal on")
        #time.sleep(0.1)
        print("slept")

