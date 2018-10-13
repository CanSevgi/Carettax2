import sys, os,importlib
from yenimotor import *
import yenimotor
if sys.version_info[0]==2 :
    from Tkinter import *
    from Tkinter import messagebox  
else :
    from tkinter import *
    from tkinter import messagebox

root = Tk()
root.state("zoomed")
root.title("Carettax2 Control Panel")

#TODO: Stat bar düzenle
stat ="None"


### Key Bindings ###

def disable_nokeypanel():
    cm1.config(state=DISABLED)
    cm2.config(state=DISABLED)
    cm3.config(state=DISABLED)
    cm4.config(state=DISABLED)
    cm5.config(state=DISABLED)
    cm6.config(state=DISABLED)
    bar1.config(state=DISABLED)
    bar2.config(state=DISABLED)
    bar3.config(state=DISABLED)
    bar4.config(state=DISABLED)
    bar5.config(state=DISABLED)
    bar6.config(state=DISABLED)
    sagorta0.config(state=DISABLED)
    sagorta30.config(state=DISABLED)
    sagorta45.config(state=DISABLED)
    sagorta60.config(state=DISABLED)
    sagorta90.config(state=DISABLED)
    solorta0.config(state=DISABLED)
    solorta30.config(state=DISABLED)
    solorta45.config(state=DISABLED)
    solorta60.config(state=DISABLED)
    solorta90.config(state=DISABLED)
    manuelbutton.config(state=DISABLED)

def enable_nokeypanel():
    cm1.config(state=NORMAL)
    cm2.config(state=NORMAL)
    cm3.config(state=NORMAL)
    cm4.config(state=NORMAL)
    cm5.config(state=NORMAL)
    cm6.config(state=NORMAL)
    bar1.config(state=NORMAL)
    bar2.config(state=NORMAL)
    bar3.config(state=NORMAL)
    bar4.config(state=NORMAL)
    bar5.config(state=NORMAL)
    bar6.config(state=NORMAL)
    sagorta0.config(state=DISABLED)
    sagorta30.config(state=DISABLED)
    sagorta45.config(state=DISABLED)
    sagorta60.config(state=DISABLED)
    sagorta90.config(state=DISABLED)
    solorta0.config(state=DISABLED)
    solorta30.config(state=DISABLED)
    solorta45.config(state=DISABLED)
    solorta60.config(state=DISABLED)
    solorta90.config(state=DISABLED)
    manuelbutton.config(state=NORMAL)


def keys():
    if keyenable.get() == 1:
        disable_nokeypanel()
        root.bind("<KeyPress-a>",sola_don)
        root.bind("<KeyRelease-a>", stop6motor)
        root.bind("<KeyPress-w>",all_forward_50)
        root.bind("<KeyRelease-w>",stop6motor)
        root.bind("<KeyPress-W>",all_forward_100)
        root.bind("<KeyRelease-W>",stop6motor)
        root.bind("<KeyPress-s>",all_backward_50)
        root.bind("<KeyRelease-s>",stop6motor)
        root.bind("<KeyPress-S>",all_backward_100)
        root.bind("<KeyRelease-S>",stop6motor)
        root.bind("<KeyPress-d>",saga_don)
        root.bind("<KeyRelease-d>",stop6motor)
        root.bind("<KeyPress-q>",sol_ileri)
        root.bind("<KeyRelease-q>", stop6motor)
        root.bind("<KeyPress-e>",sag_ileri)
        root.bind("<KeyRelease-e>", stop6motor)
        root.bind("<KeyPress-space>",stop6motor)
        root.bind("<KeyPress-Right>",kamerasaga)
        #root.bind("<KeyRelease-Right",#####)
        root.bind("<KeyPress-Left>",kamerasola)
    elif keyenable.get() == 0:
        enable_nokeypanel()

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
        motor5_reverse()
    elif cmv5.get() == 0:
        motor5_forward()
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
    s1 = IntVar(root,value=config.get("MOTORS","s1"))
    s2 = IntVar(root,value=config.get("MOTORS","s2"))
    
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

            xs1 = s1.get()
            xs2 = s2.get()

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

            config.set("MOTORS","s1",str(xs1))
            config.set("MOTORS","s2",str(xs2))            

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
    sixthframe=Frame(confi)
    sixthframe.pack()
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

    m6label = Label(sixthframe,text="Motor6").pack(side = LEFT)
    var_m6en = Entry(sixthframe,textvariable=m6en).pack(side = LEFT)
    var_m6in1 = Entry(sixthframe,textvariable=m6in1).pack(side = LEFT)
    var_m6in2 = Entry(sixthframe,textvariable=m6in2).pack(side = LEFT)

    servolabel = Label(lastFrame,text="     Sol Servo     Sağ Servo").pack()
    var_s1 = Entry(lastFrame,textvariable=s1).pack(side=LEFT)
    var_s1 = Entry(lastFrame,textvariable=s2).pack(side=LEFT)


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






revlabel = Label(root, text="Reverse").place(relx=0.17,rely=0.01)


m1label = Label(root,text="Sol Ön (1)").place(relx=0.03,rely=0.01)
bar1 = Scale(root, from_ =0, to_=100,resolution=25,orient = HORIZONTAL,length=300,command = m1scale)
bar1.place(relx=0.01,rely=0.03)
cmv1=IntVar()
cm1 = Checkbutton(root,variable=cmv1,command=reverse_motor1)
cm1.place(relx=0.17,rely=0.045)

m2label = Label(root,text="Sağ Ön (2)").place(relx=0.03,rely=0.09)
bar2 = Scale(root, from_ =0, to_=100,resolution=25,orient = HORIZONTAL,length=300,command = m2scale)
bar2.place(relx=0.01,rely=0.11)
cmv2=IntVar()
cm2 = Checkbutton(root,variable=cmv2,command=reverse_motor2)
cm2.place(relx=0.17,rely=0.125)

m3label = Label(root,text="Sol Orta (3)").place(relx=0.03,rely=0.17)
bar3 = Scale(root, from_ =0, to_=100,resolution=25,orient = HORIZONTAL,length=300,command = m3scale)
bar3.place(relx=0.01,rely=0.19)
cmv3=IntVar()
cm3 = Checkbutton(root,variable=cmv3,command=reverse_motor3)
cm3.place(relx=0.17,rely=0.205)
solorta0 = Button(text= "0°",command= lambda: solservo(500))
solorta0.place(relx=0.07,rely=0.17)
solorta30 = Button(text= "30°",command= lambda: solservo(650))
solorta30.place(relx=0.08,rely=0.17)
solorta45 = Button(text= "45°",command= lambda: solservo(800))
solorta45.place(relx=0.095,rely=0.17)
solorta60 = Button(text= "60°",command= lambda: solservo(925))
solorta60.place(relx=0.11,rely=0.17)
solorta90 = Button(text= "90°",command= lambda: solservo(1200))
solorta90.place(relx=0.125,rely=0.17)

m4label = Label(root,text="Sağ Orta (4)").place(relx=0.03,rely=0.25)
bar4 = Scale(root, from_ =0, to_=100,resolution=25,orient = HORIZONTAL,length=300,command = m4scale)
bar4.place(relx=0.01,rely=0.27)
cmv4=IntVar()
cm4 = Checkbutton(root,variable=cmv4,command=reverse_motor4)
cm4.place(relx=0.17,rely=0.285)
sagorta0 = Button(text= "0°",command= lambda: sagservo(500))
sagorta0.place(relx=0.07,rely=0.25)
sagorta30 = Button(text= "30°",command= lambda: sagservo(650))
sagorta30.place(relx=0.08,rely=0.25)
sagorta45 = Button(text= "45°",command= lambda: sagservo(800))
sagorta45.place(relx=0.095,rely=0.25)
sagorta60 = Button(text= "60°",command= lambda: sagservo(925))
sagorta60.place(relx=0.11,rely=0.25)
sagorta90 = Button(text= "90°",command= lambda: sagservo(1200))
sagorta90.place(relx=0.125,rely=0.25)

m5label = Label(root,text="Sol Arka (5)").place(relx=0.03,rely=0.33)
bar5 = Scale(root, from_ =0, to_=100,resolution=25,orient = HORIZONTAL,length=300,command = m5scale)
bar5.place(relx=0.01,rely=0.35)
cmv5=IntVar()
cm5 = Checkbutton(root,variable=cmv5,command=reverse_motor5)
cm5.place(relx=0.17,rely=0.365)

m6label = Label(root,text="Sağ Arka (6)").place(relx=0.03,rely=0.41)
bar6 = Scale(root, from_ =0, to_=100,resolution=25,orient = HORIZONTAL,length=300,command = m6scale)
bar6.place(relx=0.01,rely=0.43)
cmv6=IntVar()
cm6 = Checkbutton(root,variable=cmv6,command=reverse_motor6)
cm6.place(relx=0.17,rely=0.445)

manuelbutton = Button(text="Manuel",command=manuelwindow)
manuelbutton.place(relx=0, rely=0.95)

#FIXME: İşlevsiz buton - raspileri kapatıp tekrar açsın
resetpibutton = Button(text="Restart all system", bg = "RED")
resetpibutton.place (relx = 0.15,rely = 0.95)


confibutton = Button(text="Configuration",command=configwindow)
confibutton.place(relx=0.3,rely=0.95)

keyenabletext = Label(root,text="Enable keyboard controls :").place(relx=0.01,rely = 0.50)
keyenable = IntVar()
keyenablecheckbox = Checkbutton(root,variable=keyenable,command=keys).place(relx = 0.09, rely = 0.50)

kameratext = Label(root, text=" KAMERA " , font = "Arial 18 bold").place(relx = 0.06,rely = 0.55)



#Seperator 
Label(root,text="|").place(relx=0.2,rely = 0)
Label(root,text="|").place(relx=0.2,rely = 0.02)
Label(root,text="|").place(relx=0.2,rely = 0.04)
Label(root,text="|").place(relx=0.2,rely = 0.06)
Label(root,text="|").place(relx=0.2,rely = 0.08)
Label(root,text="|").place(relx=0.2,rely = 0.10)
Label(root,text="|").place(relx=0.2,rely = 0.12)
Label(root,text="|").place(relx=0.2,rely = 0.14)
Label(root,text="|").place(relx=0.2,rely = 0.16)
Label(root,text="|").place(relx=0.2,rely = 0.18)
Label(root,text="|").place(relx=0.2,rely = 0.20)
Label(root,text="|").place(relx=0.2,rely = 0.22)
Label(root,text="|").place(relx=0.2,rely = 0.24)
Label(root,text="|").place(relx=0.2,rely = 0.26)
Label(root,text="|").place(relx=0.2,rely = 0.28)
Label(root,text="|").place(relx=0.2,rely = 0.30)
Label(root,text="|").place(relx=0.2,rely = 0.32)
Label(root,text="|").place(relx=0.2,rely = 0.34)
Label(root,text="|").place(relx=0.2,rely = 0.36)
Label(root,text="|").place(relx=0.2,rely = 0.38)
Label(root,text="|").place(relx=0.2,rely = 0.30)
Label(root,text="|").place(relx=0.2,rely = 0.40)
Label(root,text="|").place(relx=0.2,rely = 0.42)
Label(root,text="|").place(relx=0.2,rely = 0.44)
Label(root,text="|").place(relx=0.2,rely = 0.46)
Label(root,text="|").place(relx=0.2,rely = 0.48)
Label(root,text="|").place(relx=0.2,rely = 0.40)
Label(root,text="|").place(relx=0.2,rely = 0.42)
Label(root,text="|").place(relx=0.2,rely = 0.44)
Label(root,text="|").place(relx=0.2,rely = 0.46)
Label(root,text="|").place(relx=0.2,rely = 0.48)
Label(root,text="|").place(relx=0.2,rely = 0.50)

#Orta Panel (Sensör)
sıcaklıktext = Label(root, text=" SICAKLIK " , font = "Arial 18 bold").place(relx = 0.32,rely = 0.02)
sıcaklık1 = Label(root,text="Sıcaklık 1 : .... ").place(relx = 0.27, rely = 0.06)
sıcaklık2 = Label(root,text="Sıcaklık 2 : ....").place(relx = 0.41, rely = 0.06)
sıcaklık1ort = Label(root,text="Sıcaklık 1 Son 5 data ortalaması : ....").place(relx = 0.21, rely = 0.09)
sıcaklık2ort = Label(root,text="Sıcaklık 2 Son 5 data ortalaması : ....").place(relx = 0.35, rely = 0.09)
sıcaklıktotalort = Label(root,text ="Sıcaklık 2 Net Ortalama : ....").place(relx=0.30,rely=0.12)

derinliktext = Label(root, text=" DERINLIK " , font = "Arial 18 bold").place(relx = 0.32,rely = 0.20)
derinlikanlık = Label(root,text="Anlık Derinlik : .... ").place(relx = 0.27, rely = 0.25)
derinikort = Label(root,text="3 Veri Ortalaması : .... ").place(relx = 0.38, rely = 0.25)

uzaklıktext = Label(root, text=" UZAKLIK " , font = "Arial 18 bold").place(relx = 0.32,rely = 0.33)
soluzaklık = Label(root,text="Sol Uzaklık : .... ").place(relx = 0.27, rely = 0.38)
saguzaklık = Label(root,text="Sağ Uzaklık : .... ").place(relx = 0.38, rely = 0.38)
onuzaklık = Label(root,text="Ön Uzaklık   : .... ").place(relx = 0.27, rely = 0.41)
altuzaklık =Label(root,text="Arka Uzaklık : .... ").place(relx = 0.38, rely = 0.41)

gyrotext = Label(root, text=" GYRO " , font = "Arial 18 bold").place(relx = 0.32,rely = 0.55)


status = Label(root, text=stat, bd=1,relief=SUNKEN,anchor = W)
status.pack(side=BOTTOM,fill=X)

root.mainloop()