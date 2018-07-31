from tkinter import *
pencere = Tk()
def kapat():
    if not entry.get():
        yenipen = Toplevel()
        uyari = Label(yenipen)
        uyari["text"] = "Lütfen geçerli bir e.posta adresi yazın!"
        uyari.pack()
        uybtn = Button(yenipen)
        uybtn["text"] = "Tamam"
        uybtn["command"] = yenipen.destroy
        uybtn.pack()
    else:
        pencere.destroy()
etiket = Label()
etiket["text"] = "e.posta adresiniz:"
etiket.pack()
entry = Entry()
entry.pack()
dgm = Button()
dgm["text"] = "Gönder"
dgm["command"] = kapat
dgm.pack()
pencere.mainloop()
