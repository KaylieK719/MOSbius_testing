from machine import Pin
from time import sleep_ms

# pins
sw  = Pin(13, Pin.IN, Pin.PULL_UP)
dt  = Pin(14, Pin.IN, Pin.PULL_UP)
clk = Pin(15, Pin.IN, Pin.PULL_UP)

lastClk = clk.value()

def scrolling():
    """+1 CW, -1 CCW, 0 no movement."""
    global lastClk
    dtVal  = dt.value()
    clkVal = clk.value()
    step = 0
    if lastClk == 1 and clkVal == 0:
        step =  1 if dtVal == 1 else -1
    lastClk = clkVal
    return step

def isPressed():
    if sw.value() == 0:
        sleep_ms(200)
        return True
    return False

