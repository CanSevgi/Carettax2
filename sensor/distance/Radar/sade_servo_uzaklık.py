from __future__ import print_function
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz
p.start(0.1) # Initialization - bu kısım ilk çalışma için şart

def measure():

  temperature = 30.325
  speedSound = 36288 + (0.6*temperature)
  # This function measures a distance
  GPIO.output(GPIO_TRIGGER, True)
  # Wait 10us
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()
  
  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()

  elapsed = stop-start
  distance = (elapsed * speedSound)/2

  return distance

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

time.sleep(0.5)

try:
  while True:

    i = 1
    for i in range(1,9,1): 
      p.ChangeDutyCycle(i)
      time.sleep(0.5)
      distance = measure()
      print(distance)
      time.sleep(1)
    i = 9
    for i in range(9,1,-1):
      p.ChangeDutyCycle(i)
      time.sleep(0.5)
      distance = measure()
      print(distance)
      time.sleep(1)

except KeyboardInterrupt:
  GPIO.cleanup()