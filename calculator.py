from tkinter import *
win = Tk()

def beenClicked():
    l.configure(text="1")


b1 = Button(win, text="1")
b2 = Button(win, text="2")
b3 = Button(win, text="3")
b4 = Button(win, text="4")
b5 = Button(win, text="5")
b6 = Button(win, text="6")
b7 = Button(win, text="7")
b8 = Button(win, text="8")
b9 = Button(win, text="9")
b0 = Button(win, text="0")
bdiv = Button(win, text="%")
bmul = Button(win, text="*")
badd = Button(win, text="+")
bsub = Button(win, text="-")
bequ = Button(win, text="=")
b1.grid(row=3, column=1)
b2.grid(row=3, column=2)
b3.grid(row=3, column=3)
b4.grid(row=2, column=1)
b5.grid(row=2, column=2)
b6.grid(row=2, column=3)
b7.grid(row=1, column=1)
b8.grid(row=1, column=2)
b9.grid(row=1, column=3)
b0.grid(row=4, column=2)
bdiv.grid(row=1, column=4)
bmul.grid(row=2, column=4)
badd.grid(row=4, column=4)
bsub.grid(row=3, column=4)
bequ.grid(row=4, column=3)
l = Label(win, text = "test")
l.grid(row=0, column=2)

textbox=StringVar()
textbox.set(None)
numbox = Button(win, text="test")
numbox.grid(row=5, column=5)
numbox.configure(command=beenClicked)

