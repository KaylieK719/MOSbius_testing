#Note: ADC ==> GPIO 27 (change as needed) 
from machine import ADC, Pin
from displayLCD import Display
import hardwareLCD
from ili9341 import color565
from time import sleep_ms, sleep

display = Display()
sensor = ADC(Pin(27))

def showMenu():
    display.clear()
    display.text("Testing power supply/supply protection:", 8,15)
    display.text("1.Place jumper on LDOO & V+",  35,  45)
    display.text("2.Connect LDOI to power supply", 35, 75)
    display.text("3.Supplying 3.3V to RPI Pico", 35, 105)
    sleep(5) 

def getReading(): 
    reading = sensor.read_u16()
    volts = reading * 3.3 / 65535
    print("Voltage:", volts)
    return volts 
    
def main():
    showMenu()
    reading = getReading()
    if (reading > 1.75) and (reading < 3.25): #test passed
        display.clear()
        display.text("Passed Power Test",88, 105)
        display.text("Returning to menu", 88,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        return
    
    else:
        display.clear()
        display.text("Test failed: Check connections", 40,105)
        display.text("Returning to menu", 88,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        return 

main()
