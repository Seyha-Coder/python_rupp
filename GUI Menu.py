from os import name
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
from tkinter import Listbox


root= Tk()
root.title('Group GUI Editor')
root.iconbitmap()
root.geometry("1200x660")

global open_status_name
open_status_name = False
#create New file 
def new_file():
    my_text.delete("1.0", END)
    root.title('New File- TextPad!')

#create Open file
def open_file():
    my_text.delete("1.0", END)
    #Grab filenaem
    text_file = filedialog.askopenfilename(initialdir="C:/editor/",title="Open Text File",filetypes=(("Text Files","*.txt"), ("HTLM Files", "*.html"), ("Phython Files", "*.py"), ("All File","*.*") ))
    
    if text_file:
        global open_status_name
        open_status_name = text_file
    
    #open the file
    text_file= open(text_file,'r')
    stuff = text_file.read()
    #add file to textbox
    my_text.insert(END, stuff)
    #close the open file
    text_file.close()

def save_file():
    global open_status_name
    if open_status_name:
        text_file= open(open_status_name,'w')
        text_file.write(my_text.get(1.0,END))
        text_file.close()

def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*",initialdir="C:/editor/",title="Open Text File",filetypes=(("Text Files","*.txt"), ("HTLM Files", "*.html"), ("Phython Files", "*.py"), ("All File","*.*") ))
    if text_file:
        name = text_file

        text_file = open(text_file,'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

def about(): 
    
    top = Tk()
    Lb1 = Listbox(top) 
    Lb1.insert(1, "Ing Muyleang")  
    Lb1.insert(2, "Phin Chanthy") 
    Lb1.insert(3, "Ouch Bunrey") 
    Lb1.insert(4, "Lim Sothyromnea") 
    Lb1.insert(5, "Mok Molinda") 
    Lb1.insert(6, "Peak Deth") 
    Lb1.insert(7, "Lim Sothyromnea")
    Lb1.pack() 

    
    


#create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

#create Text box
my_text= Text(my_frame, width=97,height=25,font=("Helvetica",16))
my_text.pack(pady=5)

#create meni
my_menu = Menu(root)
root.config(menu=my_menu)

#Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file )
file_menu.add_command(label="Save As", command=save_as_file)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

# Add Help
edit_help = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Help", menu=edit_help)
edit_help.add_command(label="About",command=about)




 
root.mainloop()
