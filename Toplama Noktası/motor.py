import RPi.GPIO as gpio
import time
try:
    import configparser as configparser
except ImportError:
    import ConfigParser as configparser

config = configparser.ConfigParser()
config.read('config.ini')

m1en = config.get("MOTORS","m1en")
m2en = config.get("MOTORS","m2en")
m3en = config.get("MOTORS","m3en")
m4en = config.get("MOTORS","m4en")
m5en = config.get("MOTORS","m5en")
m6en = config.get("MOTORS","m6en")

### FIXME: config.ini açılıp veri okunduğuna dair onay :

print(m1en)
print(m2en)
print(m3en)
print(m4en)
print(m5en)
print(m6en)


m1in1 = config.get("MOTORS","m1in1")
m2in1 = config.get("MOTORS","m2in1")
m3in1 = config.get("MOTORS","m3in1")
m4in1 = config.get("MOTORS","m4in1")
m5in1 = config.get("MOTORS","m5in1")
m6in1 = config.get("MOTORS","m6in1")

m1in2 = config.get("MOTORS","m1in2")
m2in2 = config.get("MOTORS","m2in2")
m3in2 = config.get("MOTORS","m3in2")
m4in2 = config.get("MOTORS","m4in2")
m5in2 = config.get("MOTORS","m5in2")
m6in2 = config.get("MOTORS","m6in2")


gpio.setmode(gpio.BCM)
#Motor1
gpio.setup(m1in1, gpio.OUT)
gpio.setup(m1in2, gpio.OUT)
gpio.output(m1in1,True)
gpio.output(m1in2,False)

gpio.setup(m1en,gpio.OUT)
m1=gpio.PWM(m1en,1000)
m1.start(0)


#Motor2
gpio.setup(m2in1, gpio.OUT)
gpio.setup(m2in2, gpio.OUT)
gpio.output(m2in1,True)
gpio.output(m2in2,False)

gpio.setup(m2en,gpio.OUT)
m2=gpio.PWM(m2en,1000)
m2.start(0)

#Motor3
gpio.setup(m3in1, gpio.OUT)
gpio.setup(m3in2, gpio.OUT)
gpio.output(m3in1,True)
gpio.output(m3in2,False)

gpio.setup(m3en,gpio.OUT)
m3=gpio.PWM(m3en,1000)
m3.start(0)

#Motor4
gpio.setup(m4in1, gpio.OUT)
gpio.setup(m4in2, gpio.OUT)
gpio.output(m4in1,True)
gpio.output(m4in2,False)

gpio.setup(m4en,gpio.OUT)
m4=gpio.PWM(m4en,1000)
m4.start(0)

#Motor5
gpio.setup(m5in1, gpio.OUT)
gpio.setup(m5in2, gpio.OUT)
gpio.output(m5in1,True)
gpio.output(m5in2,False)

gpio.setup(m5en,gpio.OUT)
m5=gpio.PWM(m5en,1000)
m5.start(0)

#Motor6
gpio.setup(m6in1, gpio.OUT)
gpio.setup(m6in2, gpio.OUT)
gpio.output(m6in1,True)
gpio.output(m6in2,False)

gpio.setup(m6en,gpio.OUT)
m6=gpio.PWM(m6en,1000)
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
    gpio.setup(m1in1, gpio.OUT)
    gpio.setup(m1in2, gpio.OUT)
    gpio.output(m1in1,True)
    gpio.output(m1in2,False)
    
    gpio.setup(m1en,gpio.OUT)
    m1=gpio.PWM(m1en,1000)
    m1.start(0)
    
    #Motor2
    gpio.setup(m2in1, gpio.OUT)
    gpio.setup(m2in2, gpio.OUT)
    gpio.output(m2in1,True)
    gpio.output(m2in2,False)
    
    gpio.setup(m2en,gpio.OUT)
    m2=gpio.PWM(m2en,1000)
    m2.start(0)
    
    #Motor3
    gpio.setup(m3in1, gpio.OUT)
    gpio.setup(m3in2, gpio.OUT)
    gpio.output(m3in1,True)
    gpio.output(m3in2,False)
    
    gpio.setup(m3en,gpio.OUT)
    m3=gpio.PWM(m3en,1000)
    m3.start(0)
    
    #Motor4
    gpio.setup(m4in1, gpio.OUT)
    gpio.setup(m4in2, gpio.OUT)
    gpio.output(m4in1,True)
    gpio.output(m4in2,False)
    
    gpio.setup(m4en,gpio.OUT)
    m4=gpio.PWM(m4en,1000)
    m4.start(0)
    
    #Motor5
    gpio.setup(m5in1, gpio.OUT)
    gpio.setup(m5in2, gpio.OUT)
    gpio.output(m5in1,True)
    gpio.output(m5in2,False)
    
    gpio.setup(m5en,gpio.OUT)
    m5=gpio.PWM(m5en,1000)
    m5.start(0)
    
    #Motor6
    gpio.setup(m6in1, gpio.OUT)
    gpio.setup(m6in2, gpio.OUT)
    gpio.output(m6in1,True)
    gpio.output(m6in2,False)
    
    gpio.setup(m6en,gpio.OUT)
    m6=gpio.PWM(m6en,1000)
    m6.start(0)


def solaci(n):
    #####Servo açı ayarlama kodları buraya#####
    n=str(n)
    print("Sol Motor "+n+"°")

def sagaci(n):
    #####Servo açı ayarlama kodları buraya#####
    n=str(n)
    print("Sağ Motor" +n+"°")