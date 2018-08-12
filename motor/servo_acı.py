import RPi.GPIO as GPIO
import time

servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 100) # GPIO 18 for PWM with 50Hz
 # Initialization - bu kısım ilk çalışma için şart

def servo(acı):
    cyclle = (int(acı) * 20)/180 #calculation of the cycle
    p.start(0)
    p.ChangeDutyCycle(cyclle)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)

try:
    while True:
        acı = input("enter acı")
        servo(acı)
        
except KeyboardInterrupt:

    GPIO.cleanup()
