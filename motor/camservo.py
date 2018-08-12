import sys, os,importlib
import time
import RPi.GPIO as gpio

servoPIN =18
gpio.setmode(gpio.BCM)
gpio.setup(servoPIN,gpio.OUT)

p = gpio.PWM(servoPIN, 100)



if sys.version_info[0]==2 :
    from Tkinter import *
    from Tkinter import messagebox  
else :
    from tkinter import *
    from tkinter import messagebox

root = Tk()
#root.state("zoomed")
root.title("Carettax2 Control Panel")

a = 930

cyclle = (int(210) * 20)/180 #calculation of the cycle
p.start(0)
p.ChangeDutyCycle(cyclle)
time.sleep(0.5)
p.ChangeDutyCycle(0)

def say(self):
    global a
    a += 5
    print(a)
    cyclle = (int(a) * 25)/1000 #calculation of the cycle
    p.ChangeDutyCycle(cyclle)
    time.sleep(0.01)
    p.ChangeDutyCycle(0)


def gerisay(self):
    global a
    a -= 5
    print(a)
    cyclle = (int(a) * 25)/1000 #calculation of the cycle
    p.ChangeDutyCycle(cyclle)
    time.sleep(0.01)
    p.ChangeDutyCycle(0)


root.bind("<KeyPress-Left>",say)
root.bind("<KeyPress-Right>",gerisay)


root.mainloop()

