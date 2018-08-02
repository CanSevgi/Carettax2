import sys
from motor import *
if sys.version_info[0]==2 :
    from Tkinter import *
else :
    from tkinter import *
from tkinter import *



root = Tk()
root.state("zoomed")
root.title("Carettax2 Control Panel")

### Key Bindings ###
""" 
def deneme(self):
    print("deneme")
root.bind("<Escape>",deneme)
"""



stat ="None"

cmv1=IntVar()
cmv2=IntVar()
cmv3=IntVar()
cmv4=IntVar()
cmv5=IntVar()
cmv6=IntVar()


def manuelwindow():
    def deneme () :
        m1man=m1var.get()
        m2man=m2var.get()
        m3man=m3var.get()
        m4man=m4var.get()
        m5man=m5var.get()
        m6man=m6var.get()
        ManSet(m1man,m2man,m3man,m4man,m5man,m6man)


    m1var=IntVar(root, value= 999)
    m2var=IntVar(root, value= 999)
    m3var=IntVar(root, value= 999)
    m4var=IntVar(root, value= 999)
    m5var=IntVar(root, value= 999)
    m6var=IntVar(root, value= 999)
    manuel=Toplevel(root)
    manuel.resizable(width=FALSE, height=FALSE)
    ######Açılacak olan manuel penceresinin konumunu ayarla tekrar !! #####
    manuel.geometry("+50+200")
    m1label = Label(manuel,text="Motor1").pack()
    m1man = Entry(manuel,textvariable=m1var).pack()
    m2label = Label(manuel,text="Motor2").pack()
    m2man = Entry(manuel,textvariable=m2var).pack()
    m3label = Label(manuel,text="Motor3").pack()
    m3man = Entry(manuel,textvariable=m3var).pack()
    m4label = Label(manuel,text="Motor4").pack()
    m4man = Entry(manuel,textvariable=m4var).pack()
    m5label = Label(manuel,text="Motor5").pack()
    m5man = Entry(manuel,textvariable=m5var).pack()
    m6label = Label(manuel,text="Motor6").pack()
    m6man = Entry(manuel,textvariable=m6var).pack()
    manuelbutton = Button(manuel,text="MANUEL PERCENTAGE",bg="Green",command = deneme).pack()




manuelbutton = Button(text="Manuel",command=manuelwindow)
manuelbutton.place(relx=0, rely=0.95)

revlabel = Label(root, text="Reverse").place(relx=0.17,rely=0.01)

m1label = Label(root,text="Sol Ön (1)").place(relx=0.03,rely=0.01)
bar1 = Scale(root,from_ =0, to_=100,orient = HORIZONTAL,length=300).place(relx=0.01,rely=0.03)
cm1 = Checkbutton(root,variable=cmv1).place(relx=0.17,rely=0.045)

m2label = Label(root,text="Sağ Ön (2)").place(relx=0.03,rely=0.09)
bar2 = Scale(root,from_ =0, to_=100,orient = HORIZONTAL,length=300).place(relx=0.01,rely=0.11)
cm2 = Checkbutton(root,variable=cmv2).place(relx=0.17,rely=0.125)

m3label = Label(root,text="Sol Orta (3)").place(relx=0.03,rely=0.17)
bar3 = Scale(root,from_ =0, to_=100,orient = HORIZONTAL,length=300).place(relx=0.01,rely=0.19)
cm3 = Checkbutton(root,variable=cmv3).place(relx=0.17,rely=0.205)
solorta0 = Button(text= "0°",command= lambda: solaci(0)).place(relx=0.07,rely=0.17)
solorta30 = Button(text= "30°",command= lambda: solaci(30)).place(relx=0.08,rely=0.17)
solorta45 = Button(text= "45°",command= lambda: solaci(45)).place(relx=0.095,rely=0.17)
solorta60 = Button(text= "60°",command= lambda: solaci(60)).place(relx=0.11,rely=0.17)
solorta90 = Button(text= "90°",command= lambda: solaci(90)).place(relx=0.125,rely=0.17)

m4label = Label(root,text="Sağ Orta (4)").place(relx=0.03,rely=0.25)
bar4 = Scale(root,from_ =0, to_=100,orient = HORIZONTAL,length=300).place(relx=0.01,rely=0.27)
cm4 = Checkbutton(root,variable=cmv4).place(relx=0.17,rely=0.285)
sagorta0 = Button(text= "0°",command= lambda: sagaci(0)).place(relx=0.07,rely=0.25)
sagorta30 = Button(text= "30°",command= lambda: sagaci(30)).place(relx=0.08,rely=0.25)
sagorta45 = Button(text= "45°",command= lambda: sagaci(45)).place(relx=0.095,rely=0.25)
sagorta60 = Button(text= "60°",command= lambda: sagaci(60)).place(relx=0.11,rely=0.25)
sagorta90 = Button(text= "90°",command= lambda: sagaci(90)).place(relx=0.125,rely=0.25)

m5label = Label(root,text="Sol Arka (5)").place(relx=0.03,rely=0.33)
bar5 = Scale(root,from_ =0, to_=100,orient = HORIZONTAL,length=300).place(relx=0.01,rely=0.35)
cm5 = Checkbutton(root,variable=cmv5).place(relx=0.17,rely=0.365)

m6label = Label(root,text="Sağ Arka (6)").place(relx=0.03,rely=0.41)
bar6 = Scale(root,from_ =0, to_=100,orient = HORIZONTAL,length=300).place(relx=0.01,rely=0.43)
cm6 = Checkbutton(root,variable=cmv6).place(relx=0.17,rely=0.445)







status = Label(root, text=stat, bd=1,relief=SUNKEN,anchor = W)
status.pack(side=BOTTOM,fill=X)

root.mainloop()