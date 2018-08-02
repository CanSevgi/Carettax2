import RPi.GPIO as GPIO
import time
import math #sin() fonksiyonu için

servoPIN = 18 #servo pini
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

PIN_TRIGGER = 4 #uzaklık pinleri
PIN_ECHO = 17

GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)



def calculateDistance(cycle):
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    #bu komutu main partta yazsak daha mı iyi olur?
    #buradaki işlevini anlayamadım
    
    time.sleep(0.001)
   
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)  
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    time.sleep(0.0001)
    
    #uzaklık hesabı
    while GPIO.input(PIN_ECHO)==0: 
        pulse_start_time = time.time()
    
    
    while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time.time()
    
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    print ("Distance:",distance,"cm")
    time.sleep(0.0006)
    
    #dikey uzaklık hesabı
    angle = math.radians((cycle * 9)/5) #angle in radian
    if angle < 90:
      realDistance = distance * math.sin(angle)
    elif angle == 90:
      realDistance = distance
    elif angle > 90:
      angle = 180 - angle
      realDistance = distance * math.sin(angle)
    return distance

p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz
p.start(1) # Initialization servo
try:
  while True:
    # i represents the duty cycle
    # açı aralığı: 14.4 - 163.8 derece
    for i in range(1,9,1): 
      p.ChangeDutyCycle(i)
      time.sleep(0.3)
      realDistance = calculateDistance(i)
      print ("Real Distance:",realDistance," cm")
    
    for i in range(9,1,-1):
      p.ChangeDutyCycle(i)
      time.sleep(0.3)
      realDistance = calculateDistance(i)
      print ("Real Distance:",realDistance," cm")
      
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()

#Bu kod çalışsa bile bir kere daha düzenlenecek
#duvar ile çember ayrımını yapması gerekiyor.
