from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

def sual():
    print("sual")
def suver():
    print("suver")


button1 = Button(topFrame, text="Su Al",bg="Green", command=sual)
button2 = Button(topFrame, text="Su Ver",bg="red",command=suver)

button1.pack()
button2.pack()


status = Label(root, text="Nothing", bd=1,relief=SUNKEN,anchor = W)
status.pack(side=BOTTOM,fill=X)
# def leftClick(event):
#     print("Left")

# def midClick(event):
#     print("mid")

# def rightClick(event):
#     print("right")



# frame = Frame(root, width = 300, height = 250)
# frame.bind("<Button-1>",leftClick)
# frame.bind("<Button-2>",midClick)
# frame.bind("<Button-3>",rightClick)
# frame.pack()

root.mainloop()