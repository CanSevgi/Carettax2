import pigpio as gpio
import time
try:
    import configparser as configparser
except ImportError:
    import ConfigParser as configparser

pi1 = pigpio.pi("169.254.160.93")#MotorPi
if not pi1.connected:
    print ("Pi1 Not Connected")

pi2 = pigpio.pi("169.254.34.191") #ServerPi
if not pi2.connected:
    print ("Pi2 Not Connected")

pi3 = pigpio.pi(".....") # CameraPi
if not pi3.connected:
    print ("Pi3 Not Connected")


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


#Motor1
pi1.set_mode(m1in1,gpio.OUTPUT)
pi1.set_mode(m1in2,gpio.OUTPUT)

pi1.write(m1in1,1)
pi1.write(m1in2,0)

pi1.set_mode(m1en,gpio.OUTPUT)
pi1.set_PWM_range(m1en,2000)
pi1.set_PWM_dutycycle(m1en,0)

#Motor2
pi1.set_mode(m2in1,gpio.OUTPUT)
pi1.set_mode(m2in2,gpio.OUTPUT)

pi1.write(m2in1,1)
pi1.write(m2in2,0)

pi1.set_mode(m2en,gpio.OUTPUT)
pi1.set_PWM_range(m2en,2000)
pi1.set_PWM_dutycycle(m2en,0)

#Motor3
pi1.set_mode(m3in1,gpio.OUTPUT)
pi1.set_mode(m3in2,gpio.OUTPUT)

pi1.write(m3in1,1)
pi1.write(m3in2,0)

pi1.set_mode(m3en,gpio.OUTPUT)
pi1.set_PWM_range(m3en,2000)
pi1.set_PWM_dutycycle(m3en,0)

#Motor4
pi1.set_mode(m4in1,gpio.OUTPUT)
pi1.set_mode(m4in2,gpio.OUTPUT)

pi1.write(m4in1,1)
pi1.write(m4in2,0)

pi1.set_mode(m4en,gpio.OUTPUT)
pi1.set_PWM_range(m4en,2000)
pi1.set_PWM_dutycycle(m4en,0)

#Motor5
pi1.set_mode(m5in1,gpio.OUTPUT)
pi1.set_mode(m5in2,gpio.OUTPUT)

pi1.write(m5in1,1)
pi1.write(m5in2,0)

pi1.set_mode(m5en,gpio.OUTPUT)
pi1.set_PWM_range(m5en,2000)
pi1.set_PWM_dutycycle(m5en,0)

#Motor6
pi1.set_mode(m6in1,gpio.OUTPUT)
pi1.set_mode(m6in2,gpio.OUTPUT)

pi1.write(m6in1,1)
pi1.write(m6in2,0)

pi1.set_mode(m6en,gpio.OUTPUT)
pi1.set_PWM_range(m6en,2000)
pi1.set_PWM_dutycycle(m6en,0)

#FIXME: SAG VE SOL SERVO PİNLERİNİ TANIMLA
# #Sol orta servo
# gpio.setup(ss1,gpio.OUT)
# s1 = gpio.PWM(ss1,100)


# #Sağ Orta Servo
# gpio.setup(ss2,gpio.OUT)
# s2 = gpio.PWM(ss2,100)


def ManSet(m1,m2,m3,m4,m5,m6):
    m1=int(m1)*20
    m2=int(m2)*20
    m3=int(m3)*20
    m4=int(m4)*20
    m5=int(m5)*20
    m6=int(m6)*20

    if m1 != 999:
        pi1.set_PWM_dutycycle(m1en,m1)
        print("M1 : " +str(m1))
    if m2 != 999 :
        pi1.ChangeDutyCycle(m2en,m2)
        print("M2 : " +str(m2))
    if m3 != 999:
        pi1.ChangeDutyCycle(m3en,m3)
        print("M3 : " +str(m3))
    if m4 != 999:
        pi1.ChangeDutyCycle(m4en,m4)
        print("M4 : " +str(m4))
    if m5 != 999:
        pi1.ChangeDutyCycle(m5en,m5)
        print("M5 : " +str(m5))
    if m6 != 999:
        pi1.ChangeDutyCycle(m6en,m6)
        print("M6 : " +str(m6))

    m1 = str(m1)
    m2 = str(m2)
    m3 = str(m3)
    m4 = str(m4)
    m5 = str(m5)
    m6 = str(m6)

    print (" M1 : %"+ m1 +"\n M2 : %"+ m2 +"\n M3 : %"+ m3 +"\n M4 : %"+ m4 +"\n M5 : %"+ m5 +"\n M6 : %"+ m6)


def reset():
    #FIXME: GPIO CLEANUP CALISMAYABILIR
    gpio.cleanup()

    #Motor1
    pi1.set_mode(m1in1,gpio.OUTPUT)
    pi1.set_mode(m1in2,gpio.OUTPUT)

    pi1.write(m1in1,1)
    pi1.write(m1in2,0)

    pi1.set_mode(m1en,gpio.OUTPUT)
    pi1.set_PWM_range(m1en,2000)
    pi1.set_PWM_dutycycle(m1en,0)

    #Motor2
    pi1.set_mode(m2in1,gpio.OUTPUT)
    pi1.set_mode(m2in2,gpio.OUTPUT)

    pi1.write(m2in1,1)
    pi1.write(m2in2,0)

    pi1.set_mode(m2en,gpio.OUTPUT)
    pi1.set_PWM_range(m2en,2000)
    pi1.set_PWM_dutycycle(m2en,0)

    #Motor3
    pi1.set_mode(m3in1,gpio.OUTPUT)
    pi1.set_mode(m3in2,gpio.OUTPUT)

    pi1.write(m3in1,1)
    pi1.write(m3in2,0)

    pi1.set_mode(m3en,gpio.OUTPUT)
    pi1.set_PWM_range(m3en,2000)
    pi1.set_PWM_dutycycle(m3en,0)

    #Motor4
    pi1.set_mode(m4in1,gpio.OUTPUT)
    pi1.set_mode(m4in2,gpio.OUTPUT)

    pi1.write(m4in1,1)
    pi1.write(m4in2,0)

    pi1.set_mode(m4en,gpio.OUTPUT)
    pi1.set_PWM_range(m4en,2000)
    pi1.set_PWM_dutycycle(m4en,0)

    #Motor5
    pi1.set_mode(m5in1,gpio.OUTPUT)
    pi1.set_mode(m5in2,gpio.OUTPUT)

    pi1.write(m5in1,1)
    pi1.write(m5in2,0)

    pi1.set_mode(m5en,gpio.OUTPUT)
    pi1.set_PWM_range(m5en,2000)
    pi1.set_PWM_dutycycle(m5en,0)

    #Motor6
    pi1.set_mode(m6in1,gpio.OUTPUT)
    pi1.set_mode(m6in2,gpio.OUTPUT)

    pi1.write(m6in1,1)
    pi1.write(m6in2,0)

    pi1.set_mode(m6en,gpio.OUTPUT)
    pi1.set_PWM_range(m6en,2000)
    pi1.set_PWM_dutycycle(m6en,0)

    #FIXME: SERVOLARSIN SET'I EKLENECEK
    print("reset")


def m1scale (val):
    x=int(val)
    pi1.set_PWM_dutycycle(m1en,x)
    print ("M1 changed to :" + str(val))

def m2scale (val):
    x=int(val)
    pi1.set_PWM_dutycycle(m2en,x)
    print ("M2 changed to :" + str(val))

def m3scale (val):
    x=int(val)
    pi1.set_PWM_dutycycle(m3en,x)
    print ("M3 changed to :" + str(val))

def m4scale (val):
    x=int(val)
    pi1.set_PWM_dutycycle(m4en,x)
    print ("M4 changed to :" + str(val))

def m5scale (val):
    x=int(val)
    pi1.set_PWM_dutycycle(m5en,x)
    print ("M5 changed to :" + str(val))

def m6scale (val):
    x=int(val)
    pi1.set_PWM_dutycycle(m6en,x)
    print ("M6 changed to :" + str(val))


def motor1_reverse () :
    pi1.write(m1in1,0)
    pi1.write(m1in2,1)

    print("M1 REVERSED")

def motor1_forward () :
    pi1.write(m1in1,1)
    pi1.write(m1in2,0)
    print("M1 FORWARD")

def motor2_reverse () :
    pi1.write(m2in1,0)
    pi1.write(m2in2,1)
    print("M2 REVERSED")

def motor2_forward () :
    pi1.write(m2in1,1)
    pi1.write(m2in2,0)
    print("M2 FORWARD")

def motor3_reverse () :
    pi1.write(m3in1,0)
    pi1.write(m3in2,1)
    print("M3 REVERSED")

def motor3_forward () :
    pi1.write(m3in1,1)
    pi1.write(m3in2,0)
    print("M3 FORWARD")

def motor4_reverse () :
    pi1.write(m4in1,0)
    pi1.write(m4in2,1)    
    print("M4 REVERSED")

def motor4_forward () :
    pi1.write(m4in1,1)
    pi1.write(m4in2,0)
    print("M4 FORWARD")

def motor5_reverse () :
    pi1.write(m5in1,0)
    pi1.write(m5in2,1)
    print("M5 REVERSED")

def motor5_forward () :
    pi1.write(m5in1,1)
    pi1.write(m5in2,0)
    print("M5 FORWARD")

def motor6_reverse () :
    pi1.write(m6in1,0)
    pi1.write(m6in2,1)
    print("M6 REVERSED")

def motor6_forward () :
    pi1.write(m6in1,1)
    pi1.write(m6in2,0)
    print("M6 FORWARD")

#FIXME:SERVO KODLARI EKLENECEK
# def solservo(x):
#     print("Sol Servo" + str(x) + "Derece")  
#     cyc = (int(x) * 20)/180 
#     s1.start(0)
#     s1.ChangeDutyCycle(cyc)
#     time.sleep(0.5)
#     s1.ChangeDutyCycle(0)
 
# def sagservo(x):
#     print("Sağ Servo" + str(x) + "Derece")     
#     cyc = (int(x) * 20)/180 
#     s2.start(0)
#     s2.ChangeDutyCycle(cyc)
#     time.sleep(0.5)
#     s2.ChangeDutyCycle(0)



##KEY BINDING FUNCTIONS

def sola_don(self):
    motor1_reverse()
    motor3_reverse()
    motor5_reverse()
    pi1.set_PWM_dutycycle(m1en,50)
    pi1.set_PWM_dutycycle(m2en,25)
    pi1.set_PWM_dutycycle(m3en,100)
    pi1.set_PWM_dutycycle(m4en,100)
    pi1.set_PWM_dutycycle(m5en,25)
    pi1.set_PWM_dutycycle(m6en,25)


def sol_ileri(self):
    motor1_reverse()
    pi1.set_PWM_dutycycle(m1en,50)
    pi1.set_PWM_dutycycle(m2en,100)
    pi1.set_PWM_dutycycle(m3en,100)
    pi1.set_PWM_dutycycle(m4en,100)
    pi1.set_PWM_dutycycle(m5en,25)
    pi1.set_PWM_dutycycle(m6en,25)

def saga_don(self):
    motor2_reverse()
    motor4_reverse()
    pi1.set_PWM_dutycycle(m1en,25)
    pi1.set_PWM_dutycycle(m2en,50)
    pi1.set_PWM_dutycycle(m3en,100)
    pi1.set_PWM_dutycycle(m4en,100)
    pi1.set_PWM_dutycycle(m5en,25)
    pi1.set_PWM_dutycycle(m6en,25)


def sag_ileri(self):
    motor2_reverse()
    pi1.set_PWM_dutycycle(m1en,100)
    pi1.set_PWM_dutycycle(m2en,50)
    pi1.set_PWM_dutycycle(m3en,100)
    pi1.set_PWM_dutycycle(m4en,100)
    pi1.set_PWM_dutycycle(m5en,25)
    pi1.set_PWM_dutycycle(m6en,25)


def all_forward_50(self):
    pi1.set_PWM_dutycycle(m1en,50)
    pi1.set_PWM_dutycycle(m2en,50)
    pi1.set_PWM_dutycycle(m3en,50)
    pi1.set_PWM_dutycycle(m4en,50)
    pi1.set_PWM_dutycycle(m5en,50)
    pi1.set_PWM_dutycycle(m6en,50)


def all_backward_50(self):
    motor1_reverse()
    motor2_reverse()
    motor3_reverse()
    motor4_reverse()
    motor5_reverse()
    motor6_reverse()
    pi1.set_PWM_dutycycle(m1en,50)
    pi1.set_PWM_dutycycle(m2en,50)
    pi1.set_PWM_dutycycle(m3en,50)
    pi1.set_PWM_dutycycle(m4en,50)
    pi1.set_PWM_dutycycle(m5en,50)
    pi1.set_PWM_dutycycle(m6en,50)


def all_forward_100 (self):
    pi1.set_PWM_dutycycle(m1en,100)
    pi1.set_PWM_dutycycle(m2en,100)
    pi1.set_PWM_dutycycle(m3en,100)
    pi1.set_PWM_dutycycle(m4en,100)
    pi1.set_PWM_dutycycle(m5en,100)
    pi1.set_PWM_dutycycle(m6en,100)
  

def all_backward_100(self):
    motor1_reverse()
    motor2_reverse()
    motor3_reverse()
    motor4_reverse()
    motor5_reverse()
    motor6_reverse()
    pi1.set_PWM_dutycycle(m1en,100)
    pi1.set_PWM_dutycycle(m2en,100)
    pi1.set_PWM_dutycycle(m3en,100)
    pi1.set_PWM_dutycycle(m4en,100)
    pi1.set_PWM_dutycycle(m5en,100)
    pi1.set_PWM_dutycycle(m6en,100)


def stop6motor(self):
    motor1_forward()
    motor2_forward()
    motor3_forward()
    motor4_forward()
    motor5_forward()
    motor6_forward()
    
    pi1.set_PWM_dutycycle(m1en,0)
    pi1.set_PWM_dutycycle(m2en,0)
    pi1.set_PWM_dutycycle(m3en,0)
    pi1.set_PWM_dutycycle(m4en,0)
    pi1.set_PWM_dutycycle(m5en,0)
    pi1.set_PWM_dutycycle(m6en,0)

