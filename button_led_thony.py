from machine import Pin
from utime import sleep

led=Pin(16,Pin.OUT)
button=Pin(5,Pin.OUT)

while True:
    
    button_state=button.value()
    if(button_state==1):
        led.value(1)
    else:
        led.value(0)