from tkinter import *

root=Tk()
root.geometry("600x500")
username=Label(root,text="Username: ").pack()
E1=Entry(root,width=50).pack()
password=Label(root,text="Password").pack()
E1=Entry(root,width=50).pack()
B1=Button(root,text="Login").pack()
root.mainloop()