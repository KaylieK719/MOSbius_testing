from machine import Pin
from time import sleep_ms

# pins
sw  = Pin(13, Pin.IN, Pin.PULL_UP)
dt  = Pin(14, Pin.IN, Pin.PULL_UP)
clk = Pin(15, Pin.IN, Pin.PULL_UP)

lastClk = clk.value()

def scrolling():
    """Return +1 for CW notch, -1 for CCW, or 0 if no movement."""
    global lastClk
    dtVal  = dt.value()
    clkVal = clk.value()
    step = 0
    if lastClk == 1 and clkVal == 0:
        step =  1 if dtVal == 1 else -1
    lastClk = clkVal
    return step

def isPressed():
    """Return True once when button is pressed (debounced)."""
    if sw.value() == 0:
        sleep_ms(200)
        return True
    return False
