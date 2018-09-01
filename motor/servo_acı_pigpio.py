import pigpio
import time
#başlatmadan önce sudo pigpiod komutunu çalıştırın
servoPIN = 18

pi = pigpio.pi() #GPIO.setmode(GPIO.BCM)

pi.set_mode(servoPIN, pigpio.OUTPUT) #GPIO.setup(servoPIN, GPIO.OUT)

#GPIO 18 for PWM with 50Hz
p = pi.set_PWM_frequency(servoPIN,100) #p = GPIO.PWM(servoPIN, 100)

def servo(acı):
    cyclle = (int(acı) * 255)/180 #calculation of the cycle
    pi.set_PWM_dutycycle(servoPIN,cyclle)
    time.sleep(0.5)


try:
    while True:
        acı = input("enter acı")
        servo(acı)
        
except KeyboardInterrupt:
    GPIO.cleanup()
