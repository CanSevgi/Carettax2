from tkinter import *
from motor import pompa,motospeed,stopall

root = Tk()
root.title("Carettax2 Control Panel")
root.geometry()

solust = Frame(root)
solust.pack()
sagust = Frame(root)
sagust.pack(side=TOP)

status = Label(root, text="Nothing", bd=1,relief=SUNKEN,anchor = W)
status.pack(side=BOTTOM,fill=X)

#####--PUMP--#####
text="Pompa"
button1 = Button(solust, text="Su Al",bg="Green", command=pompa.pump)
button2 = Button(solust, text="Stop Pumping",bg="yellow",command=pompa.stoppump)
button3 = Button(solust, text="Su Ver", bg = "red", command = pompa.depump)

#####--All Motors--#####
setbutton = Button(solust,text="Set Motors", bg="blue",command = motospeed.set)

#####--MOTOR 1--#####
text="Motor1"
m1button1 = Button(solust, text="100",bg="Green", command=motospeed.m1_100)
m1button2 = Button(solust, text="75",bg="yellow",command=motospeed.m1_75)
m1button3 = Button(solust, text="50", bg = "yellow", command = motospeed.m1_50)
m1button4 = Button(solust, text="25", bg = "yellow", command = motospeed.m1_25)
m1button5 = Button(solust, text="0", bg = "red", command = motospeed.m1_0)
m1revbutton = Button(solust, text="Reverse", bg="blue", command = motospeed.m1_rev)

#####--MOTOR 2--#####
text="Motor2"
m2button1 = Button(sagust, text="100",bg="Green", command=motospeed.m2_100)
m2button2 = Button(sagust, text="75",bg="yellow",command=motospeed.m2_75)
m2button3 = Button(sagust, text="50", bg = "yellow", command = motospeed.m2_50)
m2button4 = Button(sagust, text="25", bg = "yellow", command = motospeed.m2_25)
m2button5 = Button(sagust, text="0", bg = "red", command = motospeed.m2_0)
m2revbutton = Button(sagust, text="Reverse", bg="blue", command = motospeed.m2_rev)

#####--All--#####
stopallbutton = Button(sagust, text="STOP ALL", bg="Red",command = stopall.stop)

button1.pack()
button2.pack()
button3.pack()

m1button1.pack()
m1button2.pack()
m1button3.pack()
m1button4.pack()
m1button5.pack()
m1revbutton.pack()

m2button1.pack()
m2button2.pack()
m2button3.pack()
m2button4.pack()
m2button5.pack()
m2revbutton.pack()

stopallbutton.pack()




root.mainloop()