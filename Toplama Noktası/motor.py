import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
#Motor1
gpio.setup(26, gpio.OUT)
gpio.setup(19, gpio.OUT)
gpio.output(26,True)
gpio.output(19,False)

gpio.setup(21,gpio.OUT)
m1=gpio.PWM(21,1000)
m1.start(0)


#Motor2
gpio.setup(13, gpio.OUT)
gpio.setup(6, gpio.OUT)
gpio.output(13,True)
gpio.output(6,False)

gpio.setup(27,gpio.OUT)
m2=gpio.PWM(27,1000)
m2.start(0)

#Motor3
gpio.setup(13, gpio.OUT)
gpio.setup(6, gpio.OUT)
gpio.output(13,True)
gpio.output(6,False)

gpio.setup(27,gpio.OUT)
m3=gpio.PWM(27,1000)
m3.start(0)

#Motor4
gpio.setup(13, gpio.OUT)
gpio.setup(6, gpio.OUT)
gpio.output(13,True)
gpio.output(6,False)

gpio.setup(27,gpio.OUT)
m4=gpio.PWM(27,1000)
m4.start(0)

#Motor5
gpio.setup(13, gpio.OUT)
gpio.setup(6, gpio.OUT)
gpio.output(13,True)
gpio.output(6,False)

gpio.setup(27,gpio.OUT)
m5=gpio.PWM(27,1000)
m5.start(0)

#Motor6
gpio.setup(13, gpio.OUT)
gpio.setup(6, gpio.OUT)
gpio.output(13,True)
gpio.output(6,False)

gpio.setup(27,gpio.OUT)
m6=gpio.PWM(27,1000)
m6.start(0)




def ManSet(m1,m2,m3,m4,m5,m6):
    m1=float(m1)
    m2=float(m2)
    m3=float(m3)
    m4=float(m4)
    m5=float(m5)
    m6=float(m6)

    if m1 != 999:
        m1.ChangeDutyCycle(m1)
        print("M1 : " +str(m1))
    if m2 != 999 :
        m2.ChangeDutyCycle(m2)
        print("M2 : " +str(m2))
    if m3 != 999:
        m3.ChangeDutyCycle(m3)
        print("M3 : " +str(m3))
    if m4 != 999:
        m4.ChangeDutyCycle(m4)
        print("M4 : " +str(m4))
    if m5 != 999:
        m5.ChangeDutyCycle(m5)
        print("M5 : " +str(m5))
    if m6 != 999:
        m6.ChangeDutyCycle(m6)
        print("M6 : " +str(m6))

    m1 = str(m1)
    m2 = str(m2)
    m3 = str(m3)
    m4 = str(m4)
    m5 = str(m5)
    m6 = str(m6)

    print (" M1 : %"+ m1 +"\n M2 : %"+ m2 +"\n M3 : %"+ m3 +"\n M4 : %"+ m4 +"\n M5 : %"+ m5 +"\n M6 : %"+ m6)

def reset():
    gpio.cleanup()
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
    #Motor3
    gpio.setup(13, gpio.OUT)
    gpio.setup(6, gpio.OUT)
    gpio.output(13,True)
    gpio.output(6,False)
    
    gpio.setup(27,gpio.OUT)
    m3=gpio.PWM(27,1000)
    m3.start(0)
    
    #Motor4
    gpio.setup(13, gpio.OUT)
    gpio.setup(6, gpio.OUT)
    gpio.output(13,True)
    gpio.output(6,False)
    
    gpio.setup(27,gpio.OUT)
    m4=gpio.PWM(27,1000)
    m4.start(0)
    
    #Motor5
    gpio.setup(13, gpio.OUT)
    gpio.setup(6, gpio.OUT)
    gpio.output(13,True)
    gpio.output(6,False)
    
    gpio.setup(27,gpio.OUT)
    m5=gpio.PWM(27,1000)
    m5.start(0)
    
    #Motor6
    gpio.setup(13, gpio.OUT)
    gpio.setup(6, gpio.OUT)
    gpio.output(13,True)
    gpio.output(6,False)
    
    gpio.setup(27,gpio.OUT)
    m6=gpio.PWM(27,1000)
    m6.start(0)


def solaci(n):
    #####Servo açı ayarlama kodları buraya#####
    n=str(n)
    print("Sol Motor "+n+"°")

def sagaci(n):
    #####Servo açı ayarlama kodları buraya#####
    n=str(n)
    print("Sağ Motor" +n+"°")