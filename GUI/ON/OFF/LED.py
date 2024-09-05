import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('GUI Button ON/OFF')
root.geometry("500x500")
root.configure(background='aqua')
def onclick():
    msg = messagebox.showinfo('Button', 'Button is ON')
def offclick():
    msg = messagebox.showinfo('Button', 'Button is OFF')
ON = Button(root, text='ON', font=('Times New Roman', 18), command = onclick())
OFF = Button(root, text='OFF', font=('Times New Roman', 18), command = offclick())
ON.place(x = 150, y = 150)
OFF.place(x = 250, y = 150)