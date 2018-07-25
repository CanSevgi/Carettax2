from tkinter import *
import RPi.GPIO as gpio
import time

root = Tk()
root.title("Carettax2 Control Panel v1.0")


topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
m1var=IntVar()
m2var=IntVar()
status = Label(root, text="Nothing", bd=1,relief=SUNKEN,anchor = W)
status.pack(side=BOTTOM,fill=X)


gpio.setmode(gpio.BCM)
#Motor1
gpio.setup(26, gpio.OUT)
gpio.setup(19, gpio.OUT)
gpio.output(26,True) ##in1
gpio.output(19,False) ## in2

gpio.setup(21,gpio.OUT)##en A
m1=gpio.PWM(21,1000)
m1.start(0)


#Motor2
gpio.setup(13, gpio.OUT)##in3
gpio.setup(6, gpio.OUT) ## in4
gpio.output(13,True)
gpio.output(6,False)

gpio.setup(27,gpio.OUT)##en B
m2=gpio.PWM(27,1000)
m2.start(0)


##### -- Motor1 --#####
def m1_100():
    m1.ChangeDutyCycle(100)
    print("m1 100")

def m1_75():
    m1.ChangeDutyCycle(75)
    print("m1 75")

def m1_50():
    m1.ChangeDutyCycle(50)
    print("m1 50")

def m1_25():
    m1.ChangeDutyCycle(25)
    print("m1 25")

def m1_0():
    m1.ChangeDutyCycle(0)
    print("M2 Off")

def m1_rev():
    if gpio.output(26,True):
        gpio.output(26,False)
        gpio.output(19,True)
        print("M1 Reverse")
    elif gpio.output(26,False):
        gpio.output(26,True)
        gpio.output(19,False)
        
def manuel1(m):
    m=int(m)
    m1.ChangeDutyCycle(m)
    mm = str(m)
    print ("M1 %"+mm)

##### -- Motor2 --#####
def m2_100():
    m2.ChangeDutyCycle(100)
    print("m2 100")

def m2_75():
    m2.ChangeDutyCycle(75)
    print("m2 75")

def m2_50():
    m2.ChangeDutyCycle(50)
    print("m2 50")

def m2_25():
    m2.ChangeDutyCycle(25)
    print("m2 25")

def m2_0():
    m2.ChangeDutyCycle(0)
    print("M2 Off")

def m2_rev():
    if gpio.output(13,True):
        gpio.output(13,False)
        gpio.output(6,True)
        print("M1 Reverse")
    elif gpio.output(13,False):
        gpio.output(13,True)
        gpio.output(6,False)

def manuel2(n):
    n=int(n)
    m2.ChangeDutyCycle(n)
    nn = str(n)
    print ("M2 %"+nn)

def reset():
    gpio.cleanup()

def set():
    #####--Motor1--#####
    gpio.output(26,True)
    gpio.output(19,False)
    m1.ChangeDutyCycle(0)

    #####--Motor2--#####
    gpio.output(13,True)
    gpio.output(6,False)
    m2.ChangeDutyCycle(0)

def man():
    m = m1var.get()
    print(m)
    n = m2var.get()
    print(n)
    manuel1(m)
    manuel2(n)

#####--MOTOR 1--#####
m1label =Label(topFrame,text="Motor 1 \n Speed percentage :")
m1button1 = Button(topFrame, text="100",bg="Green", command=m1_100)
m1button2 = Button(topFrame, text="75",bg="yellow",command=m1_75)
m1button3 = Button(topFrame, text="50", bg = "yellow", command = m1_50)
m1button4 = Button(topFrame, text="25", bg = "yellow", command = m1_25)
m1button5 = Button(topFrame, text="0", bg = "red", command = m1_0)
m1revbutton = Button(topFrame, text="Reverse", bg="blue", command = m1_rev)


#####--MOTOR 2--#####
m2label =Label(topFrame,text="Motor 2 \n Speed percentage :")
m2button1 = Button(bottomFrame, text="100",bg="Green", command=m2_100)
m2button2 = Button(bottomFrame, text="75",bg="yellow",command=m2_75)
m2button3 = Button(bottomFrame, text="50", bg = "yellow", command = m2_50)
m2button4 = Button(bottomFrame, text="25", bg = "yellow", command = m2_25)
m2button5 = Button(bottomFrame, text="0", bg = "red", command = m2_0)
m2revbutton = Button(bottomFrame, text="Reverse", bg="blue", command = m2_rev)

resetbutton=Button(bottomFrame, text="RESET",bg="red", command = reset) 

m1label.pack()
m1button1.pack()
m1button2.pack()
m1button3.pack()
m1button4.pack()
m1button5.pack()
m1revbutton.pack()

m2label.pack()
m2button1.pack()
m2button2.pack()
m2button3.pack()
m2button4.pack()
m2button5.pack()
m2revbutton.pack()
resetbutton.pack()

manuellabel = Label(bottomFrame,text="Manuel Tab :").pack()
m1manuel = Entry(bottomFrame,textvariable=m1var).pack()
m2manuel = Entry(bottomFrame,textvariable=m2var).pack()
manuelbutton = Button(bottomFrame,text="MANUEL PERCENTAGE",command = man).pack()
root.mainloop()

############################################

