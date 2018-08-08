import sys, os,importlib
from motor import *
import motor
if sys.version_info[0]==2 :
    from Tkinter import *
    from Tkinter import messagebox  
else :
    from tkinter import *
    from tkinter import messagebox

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



def reverse_motor1():
    if cmv1.get() == 1:
        motor1_reverse()
    elif cmv1.get() == 0:
        motor1_forward()
    else :
        print("No Data from Reverse Motor1 Checkbox !")


def reverse_motor2():
    if cmv2.get() == 1:
        motor2_reverse()
    elif cmv2.get() == 0:
        motor2_forward()
    else :
        print("No Data from Reverse Motor2 Checkbox !")


def reverse_motor3():
    if cmv3.get() == 1:
        motor3_reverse()
    elif cmv3.get() == 0:
        motor3_forward()
    else :
        print("No Data from Reverse Motor3 Checkbox !")


def reverse_motor4():
    if cmv4.get() == 1:
       motor4_reverse()
    elif cmv4.get() == 0:
        motor4_forward()
    else :
        print("No Data from Reverse Motor4 Checkbox !")


def reverse_motor5():
    if cmv5.get() == 1:
        motor5_reverse
    elif cmv5.get() == 0:
        motor5_forward
    else :
        print("No Data from Reverse Motor5 Checkbox !")


def reverse_motor6():
    if cmv6.get() == 1:
        motor6_reverse()
    elif cmv6.get() == 0:
        motor6_forward()
    else :
        print("No Data from Reverse Motor6 Checkbox !")



def configwindow():

    config = configparser.ConfigParser()
    config.read('config.ini')

    m1en = IntVar(root,value=config.get("MOTORS","m1en"))
    m2en = IntVar(root,value=config.get("MOTORS","m2en"))
    m3en = IntVar(root,value=config.get("MOTORS","m3en"))
    m4en = IntVar(root,value=config.get("MOTORS","m4en"))
    m5en = IntVar(root,value=config.get("MOTORS","m5en"))
    m6en = IntVar(root,value=config.get("MOTORS","m6en"))
    m1in1 = IntVar(root,value=config.get("MOTORS","m1in1"))
    m2in1 = IntVar(root,value=config.get("MOTORS","m2in1"))
    m3in1 = IntVar(root,value=config.get("MOTORS","m3in1"))
    m4in1 = IntVar(root,value=config.get("MOTORS","m4in1"))
    m5in1 = IntVar(root,value=config.get("MOTORS","m5in1"))
    m6in1 = IntVar(root,value=config.get("MOTORS","m6in1"))
    m1in2 = IntVar(root,value=config.get("MOTORS","m1in2"))
    m2in2 = IntVar(root,value=config.get("MOTORS","m2in2"))
    m3in2 = IntVar(root,value=config.get("MOTORS","m3in2"))
    m4in2 = IntVar(root,value=config.get("MOTORS","m4in2"))
    m5in2 = IntVar(root,value=config.get("MOTORS","m5in2"))
    m6in2 = IntVar(root,value=config.get("MOTORS","m6in2"))
    
    def restart_program():
        importlib.reload(motor)
        python = sys.executable
        os.execl(python, python, * sys.argv)
        

    def confset():
        res = messagebox.askyesno("Program Restart", "Değişikliklerin Kaydedilmesi için programın tekrar başlatılması gerekiyor \n Onaylıyorsun Değil mi ?")
        if res :
            xm1en = m1en.get()
            xm2en = m2en.get()
            xm3en = m3en.get()
            xm4en = m4en.get()
            xm5en = m5en.get()
            xm6en = m6en.get()

            xm1in1 = m1in1.get()
            xm2in1 = m2in1.get()
            xm3in1 = m3in1.get()
            xm4in1 = m4in1.get()
            xm5in1 = m5in1.get()
            xm6in1 = m6in1.get()

            xm1in2 = m1in2.get()
            xm2in2 = m2in2.get()
            xm3in2 = m3in2.get()
            xm4in2 = m4in2.get()
            xm5in2 = m5in2.get()
            xm6in2 = m6in2.get()

            config.set('MOTORS', 'm1en', str(xm1en))
            config.set('MOTORS', 'm2en', str(xm2en))
            config.set('MOTORS', 'm3en', str(xm3en))
            config.set('MOTORS', 'm4en', str(xm4en))
            config.set('MOTORS', 'm5en', str(xm5en))
            config.set('MOTORS', 'm6en', str(xm6en))

            config.set('MOTORS', 'm1in1', str(xm1in1))
            config.set('MOTORS', 'm2in1', str(xm2in1))
            config.set('MOTORS', 'm3in1', str(xm3in1))
            config.set('MOTORS', 'm4in1', str(xm4in1))
            config.set('MOTORS', 'm5in1', str(xm5in1))
            config.set('MOTORS', 'm6in1', str(xm6in1))

            config.set('MOTORS', 'm1in2', str(xm1in2))
            config.set('MOTORS', 'm2in2', str(xm2in2))
            config.set('MOTORS', 'm3in2', str(xm3in2))
            config.set('MOTORS', 'm4in2', str(xm4in2))
            config.set('MOTORS', 'm5in2', str(xm5in2))
            config.set('MOTORS', 'm6in2', str(xm6in2))

            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            restart_program()
        else :
            messagebox.showinfo("İptal","Değişiklikler Kaydedilmedi !")
            confi.destroy()

        



    confi = Toplevel(root)
    confi.resizable(width = FALSE, height = FALSE)
    ###### TODO: Açılacak olan config penceresinin konumunu ayarla tekrar !! #####
    confi.geometry("+50+200")

    firstFrame = Frame(confi)
    firstFrame.pack()
    secondFrame = Frame(confi)
    secondFrame.pack()
    thirdFrame = Frame(confi)
    thirdFrame.pack()
    fourthFrame = Frame(confi)
    fourthFrame.pack()
    fifthFrame = Frame(confi)
    fifthFrame.pack()
    lastFrame = Frame(confi)
    lastFrame.pack()

    toplabel = Label(firstFrame, text="     Enable Pin                           In 1                                     In 2").pack()
    m1label = Label(firstFrame,text="Motor1").pack(side = LEFT)
    var_m1en = Entry(firstFrame,textvariable=m1en).pack(side = LEFT)
    var_m1in1 = Entry(firstFrame,textvariable=m1in1).pack(side = LEFT)
    var_m1in2 = Entry(firstFrame,textvariable=m1in2).pack(side = LEFT)

    m2label = Label(secondFrame,text="Motor2").pack(side = LEFT)
    var_m2en = Entry(secondFrame,textvariable=m2en).pack(side = LEFT)
    var_m2in1 = Entry(secondFrame,textvariable=m2in1).pack(side = LEFT)
    var_m2in2 = Entry(secondFrame,textvariable=m2in2).pack(side = LEFT)
    
    m3label = Label(thirdFrame,text="Motor3").pack(side = LEFT)
    var_m3en = Entry(thirdFrame,textvariable=m3en).pack(side = LEFT)
    var_m3in1 = Entry(thirdFrame,textvariable=m3in1).pack(side = LEFT)
    var_m3in2 = Entry(thirdFrame,textvariable=m3in2).pack(side = LEFT)

    m4label = Label(fourthFrame,text="Motor4").pack(side = LEFT)
    var_m4en = Entry(fourthFrame,textvariable=m4en).pack(side = LEFT)
    var_m4in1 = Entry(fourthFrame,textvariable=m4in1).pack(side = LEFT)
    var_m4in2 = Entry(fourthFrame,textvariable=m4in2).pack(side = LEFT)

    m5label = Label(fifthFrame,text="Motor5").pack(side = LEFT)
    var_m5en = Entry(fifthFrame,textvariable=m5en).pack(side = LEFT)
    var_m5in1 = Entry(fifthFrame,textvariable=m5in1).pack(side = LEFT)
    var_m5in2 = Entry(fifthFrame,textvariable=m5in2).pack(side = LEFT)

    m6label = Label(lastFrame,text="Motor6").pack(side = LEFT)
    var_m6en = Entry(lastFrame,textvariable=m6en).pack(side = LEFT)
    var_m6in1 = Entry(lastFrame,textvariable=m6in1).pack(side = LEFT)
    var_m6in2 = Entry(lastFrame,textvariable=m6in2).pack(side = LEFT)

    confibutton = Button(confi,text="Set Pins",bg="Green",command = confset).pack()


def manuelwindow():
    def ManGet () :
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
    ###### TODO: Açılacak olan manuel penceresinin konumunu ayarla tekrar !! #####
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
    manuelbutton = Button(manuel,text="MANUEL PERCENTAGE",bg="Green",command = ManGet).pack()
    resetbutton = Button(manuel,text="RESET",bg="Red",command = reset).pack()




manuelbutton = Button(text="Manuel",command=manuelwindow)
manuelbutton.place(relx=0, rely=0.95)

confibutton = Button(text="Configuration",command=configwindow)
confibutton.place(relx=0.3,rely=0.95)

revlabel = Label(root, text="Reverse").place(relx=0.17,rely=0.01)


m1label = Label(root,text="Sol Ön (1)").place(relx=0.03,rely=0.01)
bar1 = Scale(root, from_ =0, to_=100,resolution=25,orient = HORIZONTAL,length=300,command = m1scale).place(relx=0.01,rely=0.03)
cmv1=IntVar()
cm1 = Checkbutton(root,variable=cmv1,command=reverse_motor1).place(relx=0.17,rely=0.045)

m2label = Label(root,text="Sağ Ön (2)").place(relx=0.03,rely=0.09)
bar2 = Scale(root, from_ =0, to_=100,resolution=25,orient = HORIZONTAL,length=300,command = m2scale).place(relx=0.01,rely=0.11)
cmv2=IntVar()
cm2 = Checkbutton(root,variable=cmv2,command=reverse_motor2).place(relx=0.17,rely=0.125)

m3label = Label(root,text="Sol Orta (3)").place(relx=0.03,rely=0.17)
bar3 = Scale(root, from_ =0, to_=100,resolution=25,orient = HORIZONTAL,length=300,command = m3scale).place(relx=0.01,rely=0.19)
cmv3=IntVar()
cm3 = Checkbutton(root,variable=cmv3,command=reverse_motor3).place(relx=0.17,rely=0.205)
solorta0 = Button(text= "0°",command= lambda: solaci(0)).place(relx=0.07,rely=0.17)
solorta30 = Button(text= "30°",command= lambda: solaci(30)).place(relx=0.08,rely=0.17)
solorta45 = Button(text= "45°",command= lambda: solaci(45)).place(relx=0.095,rely=0.17)
solorta60 = Button(text= "60°",command= lambda: solaci(60)).place(relx=0.11,rely=0.17)
solorta90 = Button(text= "90°",command= lambda: solaci(90)).place(relx=0.125,rely=0.17)

m4label = Label(root,text="Sağ Orta (4)").place(relx=0.03,rely=0.25)
bar4 = Scale(root, from_ =0, to_=100,resolution=25,orient = HORIZONTAL,length=300,command = m4scale).place(relx=0.01,rely=0.27)
cmv4=IntVar()
cm4 = Checkbutton(root,variable=cmv4,command=reverse_motor4).place(relx=0.17,rely=0.285)
sagorta0 = Button(text= "0°",command= lambda: sagaci(0)).place(relx=0.07,rely=0.25)
sagorta30 = Button(text= "30°",command= lambda: sagaci(30)).place(relx=0.08,rely=0.25)
sagorta45 = Button(text= "45°",command= lambda: sagaci(45)).place(relx=0.095,rely=0.25)
sagorta60 = Button(text= "60°",command= lambda: sagaci(60)).place(relx=0.11,rely=0.25)
sagorta90 = Button(text= "90°",command= lambda: sagaci(90)).place(relx=0.125,rely=0.25)

m5label = Label(root,text="Sol Arka (5)").place(relx=0.03,rely=0.33)
bar5 = Scale(root, from_ =0, to_=100,resolution=25,orient = HORIZONTAL,length=300,command = m5scale).place(relx=0.01,rely=0.35)
cmv5=IntVar()
cm5 = Checkbutton(root,variable=cmv5,command=reverse_motor5).place(relx=0.17,rely=0.365)

m6label = Label(root,text="Sağ Arka (6)").place(relx=0.03,rely=0.41)
bar6 = Scale(root, from_ =0, to_=100,resolution=25,orient = HORIZONTAL,length=300,command = m6scale).place(relx=0.01,rely=0.43)
cmv6=IntVar()
cm6 = Checkbutton(root,variable=cmv6,command=reverse_motor6).place(relx=0.17,rely=0.445)

status = Label(root, text=stat, bd=1,relief=SUNKEN,anchor = W)
status.pack(side=BOTTOM,fill=X)

root.mainloop()