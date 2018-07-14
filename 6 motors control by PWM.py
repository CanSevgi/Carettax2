#This code tests L298N H-Bridge driver module with Raspberry Pi GPIO PWM connections

#gpiozero kullanımı için pip yüklenmesi gerekebilir ancak raspberry'de çalışmalı
from gpiozero import PWMOutputDevice
from time import sleep

#Defining Motor Drive GPIO Pins
#the diffirence between left1,2,3 is H-Bridges
#Motor 1 H-Bridge 1
PWM_Forward_left1_pin = 26
PWM_Reverse_left1_pin = 19
#Motor 2 H-Bridge 1
PWM_Forward_right1_pin = 13
PWM_Reverse_right1_pin = 6
#Motor 3 H-Bridge 2
PWM_Forward_left2_pin = 21
PWM_Reverse_left2_pin = 20
#Motor 4 H-Bridge 2
PWM_Forward_right2_pin = 16
PWM_Reverse_right2_pin = 12
#Motor 5 H-Bridge 3
PWM_Forward_left3_pin = 22
PWM_Reverse_left3_pin = 27
#Motor 6 H-Bridge 3
PWM_Forward_right3_pin = 23
PWM_Reverse_right3_pin = 24

#Initialise objects for H-Bridge PWM pins
#Set initial duty cycle to 0 and frequency to 1000
#Motor 1 (horizontal) H-Bridge 1
forwardLeft1 = PWMOutputDevice(PWM_Forward_left1_pin, True, 0, 1000)
reverseLeft1 = PWMOutputDevice(PWM_Reverse_left1_pin, True, 0, 1000)
#Motor 2 (horizontal) H-Bridge 1
forwardRight1 = PWMOutputDevice(PWM_Forward_right1_pin, True, 0, 1000)
reverseRight1 = PWMOutputDevice(PWM_Reverse_right1_pin, True, 0, 1000)
#Motor 3 (horizontal) H-Bridge 2
forwardLeft2 = PWMOutputDevice(PWM_Forward_left2_pin, True, 0, 1000)
reverseLeft2 = PWMOutputDevice(PWM_Reverse_left2_pin, True, 0, 1000)
#Motor 4 (horizontal) H-Bridge 2
forwardRight2 = PWMOutputDevice(PWM_Forward_right2_pin, True, 0, 1000)
reverseRight2 = PWMOutputDevice(PWM_Reverse_right2_pin, True, 0, 1000)
#Motor 5 (vertical) H-Bridge 3
forwardLeft3 = PWMOutputDevice(PWM_Forward_left3_pin, True, 0, 1000)
reverseLeft3 = PWMOutputDevice(PWM_Reverse_left3_pin, True, 0, 1000)
#Motor 6 (vertical) H-Bridge 3
forwardRight3 = PWMOutputDevice(PWM_Forward_right3_pin, True, 0, 1000)
reverseRight3 = PWMOutputDevice(PWM_Reverse_right3_pin, True, 0, 1000)

def allStop():
    forwardLeft1.value = 0
    reverseLeft1.value = 0
    forwardRight1.value = 0
    reverseRight1.value = 0
    forwardLeft2.value = 0
    reverseLeft2.value = 0
    forwardRight2.value = 0
    reverseRight2.value = 0
    forwardLeft3.value = 0
    reverseLeft3.value = 0
    forwardRight3.value = 0
    reverseRight3.value = 0

def horizontalStop():
    forwardLeft1.value = 0
    reverseLeft1.value = 0
    forwardRight1.value = 0
    reverseRight1.value = 0
    forwardLeft2.value = 0
    reverseLeft2.value = 0
    forwardRight2.value = 0
    reverseRight2.value = 0

def verticalStop():
    forwardRight3.value = 0
    reverseRight3.value = 0

def allForwardDrive():
    forwardLeft1.value = 1.0
    reverseLeft1.value = 1.0
    forwardRight1.value = 1.0
    reverseRight1.value = 1.0
    forwardLeft2.value = 1.0
    reverseLeft2.value = 1.0
    forwardRight2.value = 1.0
    reverseRight2.value = 1.0
    forwardLeft3.value = 1.0
    reverseLeft3.value = 1.0
    forwardRight3.value = 1.0
    reverseRight3.value = 1.0

def horizontalForwardDrive():
    forwardLeft1.value = 1.0
    reverseLeft1.value = 1.0
    forwardRight1.value = 1.0
    reverseRight1.value = 1.0
    forwardLeft2.value = 1.0
    reverseLeft2.value = 1.0
    forwardRight2.value = 1.0
    reverseRight2.value = 1.0

def verticalForwardDrive():
    forwardRight3.value = 1.0
    reverseRight3.value = 1.0

def allReverseDrive():
    forwardLeft1.value = 0
    reverseLeft1.value = 0
    forwardRight1.value = 0
    reverseRight1.value = 0
    forwardLeft2.value = 0
    reverseLeft2.value = 0
    forwardRight2.value = 0
    reverseRight2.value = 0
    forwardLeft3.value = 0
    reverseLeft3.value = 0
    forwardRight3.value = 0
    reverseRight3.value = 0

def horizontalReverseDrive():
    forwardLeft1.value = 0
    reverseLeft1.value = 1.0
    forwardRight1.value = 0
    reverseRight1.value = 1.0
    forwardLeft2.value = 0
    reverseLeft2.value = 1.0
    forwardRight2.value = 0
    reverseRight2.value = 1.0

def verticalReverseDrive():
    forwardRight3.value = 0
    reverseRight3.value = 1.0

#Burada forwardLeft'leri 0.2 yapmak yerine
#reverseLeft'leri 0.2 yapmayı deneyebiliriz
def forwardTurnLeft():
    forwardLeft1.value = 0.2
    reverseLeft1.value = 0
    forwardRight1.value = 0.8
    reverseRight1.value = 0
    forwardLeft2.value = 0.2
    reverseLeft2.value = 0
    forwardRight2.value = 0.8
    reverseRight2.value = 0

def forwardTurnRight():
    forwardLeft1.value = 0.8
    reverseLeft1.value = 0
    forwardRight1.value = 0.2
    reverseRight1.value = 0
    forwardLeft2.value = 0.2
    reverseLeft2.value = 0
    forwardRight2.value = 0.8
    reverseRight2.value = 0

def main():
    allStop()
    allForwardDrive()
    sleep(5)
    verticalStop()
    sleep(5)
    allReverseDrive()
    sleep(5)
    forwardTurnLeft()
    sleep(5)
    forwardTurnRight()
    sleep(5)
    allStop()

main()