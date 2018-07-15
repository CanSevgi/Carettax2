#This code tests L298N H-Bridge driver module with Raspberry Pi GPIO PWM connections


#gpiozero kullanımı için pip yüklenmesi gerekebilir ancak raspberry'de çalışmalı
from gpiozero import PWMOutputDevice
from time import sleep

#Defining Motor Drive GPIO Pins
#Motor 1
PWM_Forward_left_pin = 26
PWM_Reverse_left_pin = 19
#Motor 2
PWM_Forward_right_pin = 13
PWM_Reverse_right_pin = 6

#Initialise objects for H-Bridge PWM pins
#Set initial duty cycle to 0 and frequency to 1000
forwardLeft = PWMOutputDevice(PWM_Forward_left_pin, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_Reverse_left_pin, True, 0, 1000)

forwardRight = PWMOutputDevice(PWM_Forward_right_pin, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_Reverse_right_pin, True, 0, 1000)

def allStop():
    forwardLeft.value = 0
    reverseLeft.value = 0
    forwardRight.value = 0
    reverseRight.value = 0

def forwardDrive():
    forwardLeft.value = 1.0
    reverseLeft.value = 0
    forwardRight.value = 1.0
    reverseRight.value = 0

def reverseDrive():
    forwardLeft.value = 0
    reverseLeft.value = 1.0
    forwardRight.value = 0
    reverseRight.value = 1.0

def spinLeft():
    forwardLeft.value = 0
    reverseLeft.value = 1.0
    forwardRight.value = 1.0
    reverseRight.value = 0

def SpinRight():
    forwardLeft.value = 1.0
    reverseLeft.value = 0
    forwardRight.value = 0
    reverseRight.value = 1.0

def forwardTurnLeft():
    forwardLeft.value = 0.2
    reverseLeft.value = 0
    forwardRight.value = 0.8
    reverseRight.value = 0

def forwardTurnRight():
    forwardLeft.value = 0.8
    reverseLeft.value = 0
    forwardRight.value = 0.2
    reverseRight.value = 0

def reverseTurnLeft():
    forwardLeft.value = 0
    reverseLeft.value = 0.2
    forwardRight.value = 0
    reverseRight.value = 0.8

def reverseTurnRight():
    forwardLeft.value = 0
    reverseLeft.value = 0.8
    forwardRight.value = 0
    reverseRight.value = 0.2

def main():
    allStop()
    print("Allstop")
    forwardDrive()
    print("Forward")
    sleep(5)
    reverseDrive()
    print("reverse")
    sleep(5)
    spinLeft()
    print("spinleft")
    sleep(5)
    forwardTurnLeft()
    print("turnleft")
    sleep(5)
    forwardTurnRight()
    print("turnright")
    sleep(5)
    reverseTurnLeft()
    print("reverseturnleft")
    sleep(5)
    reverseTurnRight()
    print("reverseturnright")
    sleep(5)

    allStop()
    print("allstop")

#bu kısmı anlayamadım ??? neden if var ?
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()