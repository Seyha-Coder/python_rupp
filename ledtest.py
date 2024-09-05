
from machine import Pin
led=Pin(2,Pin.OUT)
x=int(input("Ernter number 1 or 0: "))
while x==1 or x==0:
  if x==1:
    led.on()
    x=int(input("Ernter number 1 or 0: "))
  else:
    led.off()
    x=int(input("Ernter number 1 or 0: "))