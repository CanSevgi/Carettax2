from tkinter import *
import speed

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
m1var=IntVar()
m2var=IntVar()
m = IntVar()
n = IntVar()
status = Label(root, text="Nothing", bd=1,relief=SUNKEN,anchor = W)
status.pack(side=BOTTOM,fill=X)

def man():
    m = m1manuel.get()
    n = m2manuel.get()
    speed.manuel1(m)
    speed.manuel2(n)

#####--MOTOR 1--#####
m1label =Label(topFrame,Text="Motor 1 \n Speed percentage :"+m)
m1button1 = Button(topFrame, text="100",bg="Green", command=speed.m1_100)
m1button2 = Button(topFrame, text="75",bg="yellow",command=speed.m1_75)
m1button3 = Button(topFrame, text="50", bg = "yellow", command = speed.m1_50)
m1button4 = Button(topFrame, text="25", bg = "yellow", command = speed.m1_25)
m1button5 = Button(topFrame, text="0", bg = "red", command = speed.m1_0)
m1revbutton = Button(topFrame, text="Reverse", bg="blue", command = speed.m1_rev)


#####--MOTOR 2--#####
m2label =Label(topFrame,Text="Motor 2 \n Speed percentage :"+n)
m2button1 = Button(bottomFrame, text="100",bg="Green", command=speed.m2_100)
m2button2 = Button(bottomFrame, text="75",bg="yellow",command=speed.m2_75)
m2button3 = Button(bottomFrame, text="50", bg = "yellow", command = speed.m2_50)
m2button4 = Button(bottomFrame, text="25", bg = "yellow", command = speed.m2_25)
m2button5 = Button(bottomFrame, text="0", bg = "red", command = speed.m2_0)
m2revbutton = Button(bottomFrame, text="Reverse", bg="blue", command = speed.m2_rev)

resetbutton=Button(bottomFrame, text="RESET",bg="red", command = speed.reset) 

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

manuellabel = Label(bottomFrame,Text="Manuel Tab :").pack()
m1manuel = Entry(bottomFrame,textvariable=m1var).pack()
m2manuel = Entry(bottomFrame,textvariable=m2var).pack()
manuelbutton = Button(bottomFrame,text="MANUEL PERCENTAGE",command = man()).pack()
root.mainloop()