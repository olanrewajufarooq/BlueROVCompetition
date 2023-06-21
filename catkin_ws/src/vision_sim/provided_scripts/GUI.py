import tkinter as tk
import rospy
from geometry_msgs.msg import Twist
import math
import sys
import random
import time as t

class Gui:
    def __init__(self, geometryStr, name):
       
        self.robotWindow = tk.Tk()
        self.name = name
        self.geometryStr = geometryStr
        self.robotWindow.geometry(self.geometryStr)
        self.robotWindow.title(self.name)

        self.IP = tk.Label(self.robotWindow, text=IP)

        self.Adelantebt = tk.Button(self.robotWindow, text="Adelante", command=self.adelantecb, bg='yellow')
        self.Atrasbt = tk.Button(self.robotWindow, text="Atras", command=self.atrascb, bg='yellow')
        self.Izquierdabt = tk.Button(self.robotWindow, text="Izquierda", command=self.izquierdacb, bg='yellow')
        self.Derechabt = tk.Button(self.robotWindow, text="Derecha", command=self.derechacb, bg='yellow')
        self.Stopbt = tk.Button(self.robotWindow, text="Stop", command=self.stopcb, bg='red')


        self.rotarizq = tk.Button(self.robotWindow, text="Rotar izq", command=self.rotarizqcb, bg='blue')
        self.rotardec = tk.Button(self.robotWindow, text="Rotar Dech", command=self.rotardeccb, bg='blue')
        self.subir = tk.Button(self.robotWindow, text="Subir", command=self.subcb, bg='green')
        self.bajar = tk.Button(self.robotWindow, text="Bajar", command=self.bajcb, bg='green')


        self.velocidad = tk.Label(self.robotWindow, text="Velocidad")
     
       
        self.velocidadsc = tk.Scale(self.robotWindow, resolution= 0.01, from_=0, to=1.0, orient="horizontal", command=None, length=300)
       
        

	
        self.IP.grid(row=0, column=0, columnspan=1)

        self.Adelantebt.grid(row=1, column=2, columnspan=1)
        self.Atrasbt.grid(row=3, column=2, columnspan=1)
        self.Izquierdabt.grid(row=2, column=1, columnspan=1)
        self.Derechabt.grid(row=2, column=3, columnspan=1)
        self.Stopbt.grid(row=2, column=2, columnspan=1)

        self.rotarizq.grid(row=1, column=1, columnspan=1)
        self.rotardec.grid(row=1, column=3, columnspan=1)
        self.subir.grid(row=3, column=1, columnspan=1)
        self.bajar.grid(row=3, column=3, columnspan=1)

        self.velocidad.grid(row=4, column=1, columnspan=1)
        self.velocidadsc.grid(row=4, column=2, columnspan=1)

        self.initNode()



    


    def initNode(self):
        rospy.init_node('simula_envio', anonymous=True)
        self.pub = rospy.Publisher(IP, Twist, queue_size=10)

        self.time_to_sleep = 0
        self.ref_time = 0

        # ROS =========================================

        print("OK")
 


    def rotarizqcb(self):
        mov = Twist()
        mov.angular.z = -self.velocidadsc.get()
        self.pub.publish(mov)
    def rotardeccb(self):
        mov = Twist()
        mov.angular.z = self.velocidadsc.get()
        self.pub.publish(mov)
    def subcb(self):
        mov = Twist()
        mov.linear.z = self.velocidadsc.get()
        self.pub.publish(mov)
    def bajcb(self):
        mov = Twist()
        mov.linear.z = -self.velocidadsc.get()
        self.pub.publish(mov)

    def adelantecb(self):
        mov = Twist()
        mov.linear.x = self.velocidadsc.get()
        self.pub.publish(mov)

    def atrascb(self):
        mov = Twist()
        mov.linear.x = -self.velocidadsc.get()
        self.pub.publish(mov)
    def izquierdacb(self):
        mov = Twist()
        mov.linear.y = -self.velocidadsc.get()
        self.pub.publish(mov)
    def derechacb(self):
        mov = Twist()
        mov.linear.y = self.velocidadsc.get()
        self.pub.publish(mov)
    def stopcb(self):
        mov = Twist()
        self.pub.publish(mov)


		
		


if __name__ == "__main__":

   
 

    IP = "/cmd_vel"

    c1 = Gui("550x600+640+0","gui")
    c1.robotWindow.mainloop()

