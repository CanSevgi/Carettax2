import RPi.GPIO as gpio
import time
try:
    import configparser as configparser
except ImportError:
    import ConfigParser as configparser



print("motor.py imported without error")

config = configparser.ConfigParser()
config.read('config.ini')

m1en = int(config.get("MOTORS","m1en"))
m2en = int(config.get("MOTORS","m2en"))
m3en = int(config.get("MOTORS","m3en"))
m4en = int(config.get("MOTORS","m4en"))
m5en = int(config.get("MOTORS","m5en"))
m6en = int(config.get("MOTORS","m6en"))


m1in1 = int(config.get("MOTORS","m1in1"))
m2in1 = int(config.get("MOTORS","m2in1"))
m3in1 = int(config.get("MOTORS","m3in1"))
m4in1 = int(config.get("MOTORS","m4in1"))
m5in1 = int(config.get("MOTORS","m5in1"))
m6in1 = int(config.get("MOTORS","m6in1"))

m1in2 = int(config.get("MOTORS","m1in2"))
m2in2 = int(config.get("MOTORS","m2in2"))
m3in2 = int(config.get("MOTORS","m3in2"))
m4in2 = int(config.get("MOTORS","m4in2"))
m5in2 = int(config.get("MOTORS","m5in2"))
m6in2 = int(config.get("MOTORS","m6in2"))

ss1 = int(config.get("MOTORS","s1"))
ss2 = int(config.get("MOTORS","s2"))


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

#TODO: Servo pinlerini config'e ekle
#Sol orta servo
gpio.setup(ss1,gpio.OUT)
s1 = gpio.PWM(ss1,50)
s1.start(0)

#Sağ Orta Servo
gpio.setup(ss2,gpio.OUT)
s2 = gpio.PWM(ss2,50)
s2.start(0)


def ManSet(m1,m2,m3,m4,m5,m6):
    m1=int(m1)
    m2=int(m2)
    m3=int(m3)
    m4=int(m4)
    m5=int(m5)
    m6=int(m6)

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

    #Sol orta servo
    gpio.setup(ss1,gpio.OUT)
    s1 = gpio.PWM(ss1,50)

    #Sağ Orta Servo
    gpio.setup(ss2,gpio.OUT)
    s2 = gpio.PWM(ss2,50)

    print("reset")

def m1scale (val):
    x=int(val)
    m1.ChangeDutyCycle(x)
    print ("M1 changed to :" + str(val))

def m2scale (val):
    x=int(val)
    m2.ChangeDutyCycle(x)
    print ("M2 changed to :" + str(val))

def m3scale (val):
    x=int(val)
    m3.ChangeDutyCycle(x)
    print ("M3 changed to :" + str(val))

def m4scale (val):
    x=int(val)
    m4.ChangeDutyCycle(x)
    print ("M4 changed to :" + str(val))

def m5scale (val):
    x=int(val)
    m5.ChangeDutyCycle(x)
    print ("M5 changed to :" + str(val))

def m6scale (val):
    x=int(val)
    m6.ChangeDutyCycle(x)
    print ("M6 changed to :" + str(val))


def motor1_reverse () :
    gpio.output(m1in1,False)
    gpio.output(m1in2,True)
    print("M1 REVERSED")

def motor1_forward () :
    gpio.output(m1in1,True)
    gpio.output(m1in2,False)
    print("M1 FORWARD")

def motor2_reverse () :
    gpio.output(m2in1,False)
    gpio.output(m2in2,True)
    print("M2 REVERSED")

def motor2_forward () :
    gpio.output(m2in1,True)
    gpio.output(m2in2,False)
    print("M2 FORWARD")

def motor3_reverse () :
    gpio.output(m3in1,False)
    gpio.output(m3in2,True)
    print("M3 REVERSED")

def motor3_forward () :
    gpio.output(m3in1,True)
    gpio.output(m3in2,False)
    print("M3 FORWARD")

def motor4_reverse () :
    gpio.output(m4in1,False)
    gpio.output(m4in2,True)
    print("M4 REVERSED")

def motor4_forward () :
    gpio.output(m4in1,True)
    gpio.output(m4in2,False)
    print("M4 FORWARD")

def motor5_reverse () :
    gpio.output(m5in1,False)
    gpio.output(m5in2,True)
    print("M5 REVERSED")

def motor5_forward () :
    gpio.output(m5in1,True)
    gpio.output(m5in2,False)
    print("M5 FORWARD")

def motor6_reverse () :
    gpio.output(m6in1,False)
    gpio.output(m6in2,True)
    print("M6 REVERSED")

def motor6_forward () :
    gpio.output(m6in1,True)
    gpio.output(m6in2,False)
    print("M6 FORWARD")


def solservo(x):
    print("Sol Servo" + str(x) + "Derece")  
    cyc = (int(x) * 10)/180

    s1.ChangeDutyCycle(cyc)
    time.sleep(0.5)
 
def sagservo(x):
    print("Sağ Servo" + str(x) + "Derece")     

    cyc = (int(x) * 10)/180

    s2.ChangeDutyCycle(cyc)
    time.sleep(0.5)


##KEY BINDING FUNCTIONS

def sola_don(self):
    motor1_reverse()
    motor3_reverse()
    motor5_reverse()
    m1.ChangeDutyCycle(50)
    m2.ChangeDutyCycle(25)
    m3.ChangeDutyCycle(100)
    m4.ChangeDutyCycle(100)
    m5.ChangeDutyCycle(25)
    m6.ChangeDutyCycle(25)

def sol_ileri(self):
    motor1_reverse()
    m1.ChangeDutyCycle(50)
    m2.ChangeDutyCycle(100)
    m3.ChangeDutyCycle(100)
    m4.ChangeDutyCycle(100)
    m5.ChangeDutyCycle(25)
    m6.ChangeDutyCycle(25)

def saga_don(self):
    motor2_reverse()
    motor4_reverse()
    m1.ChangeDutyCycle(25)
    m2.ChangeDutyCycle(50)
    m3.ChangeDutyCycle(100)
    m4.ChangeDutyCycle(100)
    m5.ChangeDutyCycle(25)
    m6.ChangeDutyCycle(25)

def sag_ileri(self):
    motor2_reverse()
    m1.ChangeDutyCycle(100)
    m2.ChangeDutyCycle(50)
    m3.ChangeDutyCycle(100)
    m4.ChangeDutyCycle(100)
    m5.ChangeDutyCycle(25)
    m6.ChangeDutyCycle(25)

def all_forward_50(self):
    m1.ChangeDutyCycle(50)
    m2.ChangeDutyCycle(50)
    m3.ChangeDutyCycle(50)
    m4.ChangeDutyCycle(50)
    m5.ChangeDutyCycle(50)
    m6.ChangeDutyCycle(50)

def all_backward_50(self):
    motor1_reverse()
    motor2_reverse()
    motor3_reverse()
    motor4_reverse()
    motor5_reverse()
    motor6_reverse()
    m1.ChangeDutyCycle(50)
    m2.ChangeDutyCycle(50)
    m3.ChangeDutyCycle(50)
    m4.ChangeDutyCycle(50)
    m5.ChangeDutyCycle(50)
    m6.ChangeDutyCycle(50)

def all_forward_100 (self):
    m1.ChangeDutyCycle(100)
    m2.ChangeDutyCycle(100)
    m3.ChangeDutyCycle(100)
    m4.ChangeDutyCycle(100)
    m5.ChangeDutyCycle(100)
    m6.ChangeDutyCycle(100)    

def all_backward_100(self):
    motor1_reverse()
    motor2_reverse()
    motor3_reverse()
    motor4_reverse()
    motor5_reverse()
    motor6_reverse()
    m1.ChangeDutyCycle(100)
    m2.ChangeDutyCycle(100)
    m3.ChangeDutyCycle(100)
    m4.ChangeDutyCycle(100)
    m5.ChangeDutyCycle(100)
    m6.ChangeDutyCycle(100)


def stop6motor(self):
    motor1_forward()
    motor2_forward()
    motor3_forward()
    motor4_forward()
    motor5_forward()
    motor6_forward()
    
    m1.ChangeDutyCycle(0)
    m2.ChangeDutyCycle(0)
    m3.ChangeDutyCycle(0)
    m4.ChangeDutyCycle(0)
    m5.ChangeDutyCycle(0)
    m6.ChangeDutyCycle(0)
