#Server
import time
import logging
import threading
import BaseHTTPServer
from pymavlink import mavutil
import keyboard as key
import urlparse
import random
import tkinter as tk
from flask import Flask, render_template
#from gui_brov import arm, disarm, lights_on, lights_off, right, left, forward, backward, up, down, rot_left, rot_right
HOST_NAME = 'localhost' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 8088 # Maybe set this to 9000.

global speed
global timer
global depth
global speed_neg
global depth_neg
global kpress

global x
global y
global z
global i
global rotation

kpress=False
speed = 500
speed_neg=-speed
depth=0.5*speed+500
depth_neg=0.5*speed_neg+500

#timer = 10;
x = 0;
y = 0;
z = 500;
i = 0;
rotation = 0;
#speed = 200

def arm():
	master.arducopter_arm()
	print("Vehicle armed")
def disarm():
	master.arducopter_disarm()
	print("Vehicle disarmed")


def lights_on():
	master.mav.manual_control_send(
            master.target_system,
            0, #x
            0,#y
            500, #z
            0, #rotation
            1<<14) #active button
            #time.sleep(0.1)

def lights_off():
	master.mav.manual_control_send(
            master.target_system,
            0, #x
            0, #y
            500, #z
            0, #rotation
            1<<13) #active button
            #time.sleep(0.1)
        
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def roll():
        lbl_result["text"] = str(random.randint(1, 6))

    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
	start_time = time.time()
        """Respond to a GET request."""
	kpress=False
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>BlueROV server.</title></head>")
        s.wfile.write("<body><p>BlueROV server.</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        s.wfile.write("<p>You accessed path: %s</p>" % s.path)
        s.wfile.write("</body></html>")
	
	# Read the input after the query (?)
        inputQueryStr = urlparse.urlparse(s.path).query
	mode = urlparse.parse_qs(inputQueryStr).get('mode', 0)
        modes = mode[0]

        time_input = urlparse.parse_qs(inputQueryStr).get('time', 0)
	timer_string = time_input[0]
	
	timer_mili = float(timer_string)
	#timer = timer_mili
	timer = timer_mili*10
	
	#speed_input = urlparse.parse_qs(inputQueryStr).get('speed', 0)
	#speed_string = speed_input[0]
	#speed = float(speed_string)

	#print("Selected speed: ", speed)
        print("BlueROV will operate for:" ,timer)
	print("Mode selected:"+modes)
        
	#ARM /DISARM
	if (modes == "arm"):
	    #print("do_Get:"+inputQueryStr)
            arm()
	elif (modes == "disarm"):
            #print("do_Get:"+inputQueryStr)
            disarm()

	#LIGHTS ON
        if(modes == "lightson"):
    	    lights_on()

	#LIGHTS OFF
        if(modes == "lightsoff"):
    	    lights_off()

	#ROTATION
        if(modes == "rotate_right"):
	    x=0
	    y=0
	    z=500
	    rotation=speed
	    kpress=True
	    e=0
	elif(modes == "rotate_left"):
	    x=0
	    y=0
	    z=500
	    rotation=-speed
	    kpress=True
	    e=0
	else:
	    rotation=0

	#MOVE IN X (FRONT/BACK)
	if(modes == "forward"):
	    x=speed
	    y=0
	    z=500
	    rotation=0
	    kpress=True
	    e=0
	elif(modes == "backward"):
	    x=-speed
	    y=0
	    z=500
	    rotation=0
	    kpress=True
	    e=0
	else:
	    x=0

	#MOVE IN Y (RIGHT/LEFT)
	if(modes == "right"):
	    x=0
	    y=speed
	    z=500
	    rotation=0
	    kpress=True
	    e=0
	elif(modes == "left"):
	    x=0
	    y=-speed
	    z=500
	    rotation=0
	    kpress=True
	    e=0
	else:
	    y=0

	#MOVE IN Z (UP/DOWN)
	if(modes == "up"):
	    x=0
	    y=0
	    z=depth
	    rotation=0
	    kpress=True
	    e=0
	elif(modes == "down"):
	    x=0
	    y=0
	    z=depth_neg
	    rotation=0
	    kpress=True
	    e=0
	else:
	    z=500

        while(kpress==True):
            master.mav.manual_control_send(
                master.target_system,
                x, #x
                y, #y
                z, #z
                rotation, #rotation
                0) #active button
	    if(e>=timer):
		break
	    e=e+1
	    #print(e)
	    print("Tiempo estimado de ejecucion:", timer_mili)
	    print("x:", x)
	    print("y:", y)
	    print("z:",z)
	    print("rotation:",rotation)	
	    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':

    #master = mavutil.mavlink_connection('udpin:192.168.2.1:14550')
    master = mavutil.mavlink_connection('udpin:127.0.0.1:14551')
    master.wait_heartbeat()
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
       
    
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
