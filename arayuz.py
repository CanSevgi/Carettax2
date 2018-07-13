from tkinter import *
import pompa

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)



button1 = Button(topFrame, text="Su Al",bg="Green", command=pompa.pump)
button2 = Button(topFrame, text="Stop Pumping",bg="yellow",command=pompa.stoppump)
button3 = Button(topFrame, text="Su Ver", bg = "red", command = pompa.depump)

button1.pack()
button2.pack()
button3.pack()


status = Label(root, text="Nothing", bd=1,relief=SUNKEN,anchor = W)
status.pack(side=BOTTOM,fill=X)


root.mainloop()