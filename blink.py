from machine import Pin, Timer
import machine
#led pin on the board only for Pico W, Pin 25 for non-W
led = machine.Pin("LED", machine.Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()
    
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)