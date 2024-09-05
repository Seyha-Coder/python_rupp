#button+message box
import time
from tkinter import *
from tkinter import messagebox
top= Tk()
top.title('GUI Button ON/OFF')
top.geometry("400x400")
top.configure(background='blue')
def onclick():
    msg=messagebox.showinfo("Button","Button is ON")
def offclick():
    msg=messagebox.showinfo("Button","Button is OFF")
ON=Button(top,text="ON",font=("helveita",18), command=onclick())
OFF=Button(top,text="OFF",font=("helveita",18), command=offclick())
ON.place(x=100,y=100)
OFF.place(x=200,y=100)
top.mainloop()
