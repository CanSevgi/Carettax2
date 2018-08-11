import RPi.GPIO as GPIO
import time

servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz
p.start(0.1) # Initialization - bu kısım ilk çalışma için şart

def servo(acı):
    cyclle = (int(acı) * 10)/180 #calculation of the cycle

    p.ChangeDutyCycle(cyclle)
    time.sleep(0.5)

try:
    while True:
        acı = input("enter acı")
        servo(acı)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()