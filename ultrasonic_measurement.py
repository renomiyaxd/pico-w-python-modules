from machine import Pin
import time
import utime
led = machine.Pin("LED", machine.Pin.OUT)

trigger = Pin(2,Pin.OUT) #refer to GPIO number
echo = Pin(3,Pin.IN) #refer to GPIO number


#Gets distance from Ultrasonic sensor, not need to change
def getDist():
    trigger.low()
    utime.sleep_us(2)  #Delay for 2 microseconds
    trigger.high()
    utime.sleep_us(5)  #Delay for 2 microseconds
    trigger.low()
    
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    
    while echo.value() == 1:
        signalon = utime.ticks_us()
        
    timepassed = signalon - signaloff    
    distance = (timepassed * 0.0343)/2
    return distance


#def to be called to get the distance and acceleration relative
#to oncoming obstacle. Can be changed
def run():
    d1 = getDist()
    time.sleep(0.5)
    d2 = getDist()
    
    ac = d1-d2
    print(d1,",",d2,",",ac)
    
    if (ac > 1) and (d2 < 50):
        led(1)
        print("Stopped 1!")
        time.sleep(5)
        led(0)
    elif (d2 < 20):
        led(1)
        print("Stopped 2!")
        time.sleep(5)
        led(0)
        
while True:
    run()