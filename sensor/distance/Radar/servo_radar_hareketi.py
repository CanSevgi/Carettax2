import RPi.GPIO as GPIO
import time

servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz
p.start(0.1) # Initialization - bu kısım ilk çalışma için şart

try:
  while True:
    # i represents the duty cycle
    # açı aralığı: 14.4 - 163.8 derece
    i = 1
    for i in range(1,9,1): 
      p.ChangeDutyCycle(i)
      time.sleep(0.5)
    i = 9
    for i in range(9,1,-1):
      p.ChangeDutyCycle(i)
      time.sleep(0.5)
except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  p.stop()
  GPIO.cleanup()