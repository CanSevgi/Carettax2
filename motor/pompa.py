import RPi.GPIO as gpio
import time
 

def init():
 gpio.setmode(gpio.BCM)
 #Motor1
 gpio.setup(17, gpio.OUT)
 gpio.setup(22, gpio.OUT)

 #Motor2
 gpio.setup(23, gpio.OUT)
 gpio.setup(24, gpio.OUT)
 
def pump():
 init()
 print ("Motor1 Forward Motor2 Off")
 #Motor1 (Forward)
 gpio.output(17, False)
 gpio.output(22, True)

#Motor2 (Off)
 gpio.output(23, False) 
 gpio.output(24, False)
 
 
def depump():
 init()
 print ("Motor1 Reverse Motor2 Off")
 #Motor 1 (Reverse)
 gpio.output(17, True)
 gpio.output(22, False)

#Motor2 (off)
 gpio.output(23, False) 
 gpio.output(24, False)

def stoppump():
    init()
    #Motor1 (Off)
    gpio.output(17, False)
    gpio.output(22, False)

    #Motor2 (Off)
    #gpio.output(23, False) 
    #gpio.output(24, False)
 