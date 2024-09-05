from machine import Pin
led=Pin(2,Pin.OUT)
for i in range(0,100) :
    print(i)
    led.on()