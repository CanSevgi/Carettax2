from __future__ import print_function
import time
import RPi.GPIO as GPIO
import math

#bu kodun farkı 3 ölçümün ortalamasını görüntlüyor

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz
p.start(0.1) # Initialization - bu kısım ilk çalışma için şart

def measure(cyclee):
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
  print(distance)

  #dikey uzaklık hesabı
  angle = math.radians((cyclee * 9)/5) #angle in radian
  if angle < 90:
    realDistance = distance * math.sin(angle)
  elif angle == 90:
    realDistance = distance
  elif angle > 90:
    angle = 180 - angle
    realDistance = distance * math.sin(angle)
  return distance

def measure_average(cycle):
  # This function takes 3 measurements and
  # returns the average.

  distance1=measure(cycle)
  time.sleep(0.1)
  distance2=measure(cycle)
  time.sleep(0.1)
  distance3=measure(cycle)
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance

# Speed of sound in cm/s at temperature
temperature = 30.325
speedSound = 36288 + (0.6*temperature)
# havada ve 30.625 derecede 36288
#print("Ultrasonic Measurement")
#print("Speed of sound is",speedSound/100,"m/s at ",temperature,"deg")

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

# Allow module to settle
time.sleep(0.5)

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:
  while True:
    
    # i represents the duty cycle
    # açı aralığı: 14.4 - 163.8 derece
    i = 1
    for i in range(1,9,1): 
      p.ChangeDutyCycle(i)
      time.sleep(0.5)
      distance = measure_average(i)
      print("Real Distance : {0:5.1f}".format(distance))
      time.sleep(1)
    i = 9
    for i in range(9,1,-1):
      p.ChangeDutyCycle(i)
      time.sleep(0.5)
      distance = measure_average(i)
      print("Real Distance : {0:5.1f}".format(distance))
      time.sleep(1)

except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  GPIO.cleanup()