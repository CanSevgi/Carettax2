#!/usr/bin/python
#encoding:utf-8

import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

TRIG = 15                                  #Associate pin 15 to TRIG
ECHO = 14                                  #Associate pin 14 to Echo

print ("Distance measurement in progress")

GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in

while True:

  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  print ("Waiting For Sensor To Settle")
  time.sleep(2)                            #Delay of 2 seconds

  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO)==0:               #Check if Echo is LOW
    pulse_start = time.time()              #Time of the last  LOW pulse

  while GPIO.input(ECHO)==1:               #Check whether Echo is HIGH
    pulse_end = time.time()                #Time of the last HIGH pulse 

  pulse_duration = pulse_end - pulse_start #pulse duration to a variable

  distance = pulse_duration * 17150        #Calculate distance
  distance = round(distance, 2)            #Round to two decimal points

  if distance > 20 and distance < 400:     #Is distance within range
    print ("Distance:",distance - 0.5,"cm")  #Distance with calibration
  else:
    print ("Out Of Range")                   #display out of range