import RPi.GPIO as GPIO
import time

try:
      GPIO.setmode(GPIO.BOARD)### DIKKAT BOARD PINLERI !!! ###

      PIN_TRIGGER = 12 #gpio 18
      PIN_ECHO = 11 #gpio 17

      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      print "Waiting for sensor to settle"

      time.sleep(0.5)

      print "Calculating distance"

      GPIO.output(PIN_TRIGGER, GPIO.HIGH)

      time.sleep(0.00001)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)
      pulse_start_time = time.time()

      while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
      while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

      pulse_duration = pulse_end_time - pulse_start_time
      distance = round(pulse_duration * 17150, 2)
      print "Distance:",distance,"cm"

finally:
      GPIO.cleanup()

# https://pimylifeup.com/raspberry-pi-distance-sensor/