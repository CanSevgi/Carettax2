import RPi.GPIO as gpio

def stop():
    #####--Pump Stop--#####
    gpio.output(17, False)
    gpio.output(22, False)
    
    #####--Motor1 Stop--#####
    gpio.output(26,False)
    gpio.output(19,False)
    
    #####--Motor2 Stop--#####
    gpio.output(13,False)
    gpio.output(6,False)