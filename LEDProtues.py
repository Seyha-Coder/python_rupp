import serial
import time
from tkinter import *
from serial import Serial
# from serial import serial


ArduinoSerial = serial.Serial('COM1', 9600, timeout=1)
time.sleep(2)  # delay 2s
status1 = 0


def clickon():
    ArduinoSerial.write(b'1')
    1


def clickoff():
    ArduinoSerial.write(b'0')
    0


def exit_p():
    ArduinoSerial.write(b'0')
    0


# status1 = "Quit“
quit()
top= Tk()
top.title('GUI Button ON/OFF')
top.geometry("500x400")
top.configure(background='yellow')


Button_ON=Button(top,text="ON",font=("helveita",18),command=clickon)


Button_OFF=Button(top,text="OFF",font=("helveita",18),command=clickoff)


Button_exit=Button(top,text="Exit",font=("helveita",18),command=exit_p)
Button_ON.place(x=100,y=100)
Button_OFF.place(x=200,y=100)
Button_exit.place(x=320,y=100)
