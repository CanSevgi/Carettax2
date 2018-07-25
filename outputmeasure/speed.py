import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
#Motor1
gpio.setup(26, gpio.OUT)
gpio.setup(19, gpio.OUT)
gpio.output(26,True) ##in1
gpio.output(19,False) ## in2

gpio.setup(21,gpio.OUT)##en A
m1=gpio.PWM(21,1000)
m1.start(0)


#Motor2
gpio.setup(13, gpio.OUT)##in3
gpio.setup(6, gpio.OUT) ## in4
gpio.output(13,True)
gpio.output(6,False)

gpio.setup(27,gpio.OUT)##en B
m2=gpio.PWM(27,1000)
m2.start(0)


##### -- Motor1 --#####
def m1_100():
    m1.ChangeDutyCycle(100)
    print("m1 100")

def m1_75():
    m1.ChangeDutyCycle(75)
    print("m1 75")

def m1_50():
    m1.ChangeDutyCycle(50)
    print("m1 50")

def m1_25():
    m1.ChangeDutyCycle(25)
    print("m1 25")

def m1_0():
    m1.ChangeDutyCycle(0)
    print("M2 Off")

def m1_rev():
    if gpio.output(26,True):
        gpio.output(26,False)
        gpio.output(19,True)
        print("M1 Reverse")
    elif gpio.output(26,False):
        gpio.output(26,True)
        gpio.output(19,False)
        
def manuel1(m):
    m2.ChangeDutyCycle(m)
    print ("M1 %"+m)

##### -- Motor2 --#####
def m2_100():
    m2.ChangeDutyCycle(100)
    print("m2 100")

def m2_75():
    m2.ChangeDutyCycle(75)
    print("m2 75")

def m2_50():
    m2.ChangeDutyCycle(50)
    print("m2 50")

def m2_25():
    m2.ChangeDutyCycle(25)
    print("m2 25")

def m2_0():
    m2.ChangeDutyCycle(0)
    print("M2 Off")

def m2_rev():
    if gpio.output(13,True):
        gpio.output(13,False)
        gpio.output(6,True)
        print("M1 Reverse")
    elif gpio.output(13,False):
        gpio.output(13,True)
        gpio.output(6,False)

def manuel2(n):
    m2.ChangeDutyCycle(n)
    print ("M2 %"+n)

def reset():
    gpio.cleanup()

def set():
    #####--Motor1--#####
    gpio.output(26,True)
    gpio.output(19,False)
    m1.ChangeDutyCycle(0)

    #####--Motor2--#####
    gpio.output(13,True)
    gpio.output(6,False)
    m2.ChangeDutyCycle(0)