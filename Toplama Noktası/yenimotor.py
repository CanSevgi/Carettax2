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



pi1.set_mode(m1in1,gpio.OUTPUT)
pi1.set_mode(m1in1,gpio.OUTPUT)
pi1.set_mode(m1in1,gpio.OUTPUT)
pi1.set_mode(m1in1,gpio.OUTPUT)
pi1.set_mode(m1in1,gpio.OUTPUT)
pi1.set_mode(m1in1,gpio.OUTPUT)
pi1.set_mode(m1in1,gpio.OUTPUT)
pi1.set_mode(m1in1,gpio.OUTPUT)
pi1.set_mode(m1in1,gpio.OUTPUT)
pi1.set_mode(m1in1,gpio.OUTPUT)
pi1.set_mode(m1in1,gpio.OUTPUT)


