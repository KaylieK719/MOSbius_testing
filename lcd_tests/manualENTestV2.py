from machine import ADC, Pin
from displayLCD import Display
import hardwareLCD
from ili9341 import color565
from time import sleep_ms, sleep

display = Display()
sensor = ADC(Pin(27)) #ADC GPIO27 (Pin 32)

def showMenu():
    display.clear()
    display.text("Testing manual enable:", 8,15)
    display.text("1.Place jumper on EM_PU",  35,  45)
    display.text("2.Connect LDOI to power supply", 35, 75)
    display.text("3.Place jumper on GPIO27 & EM pin", 35, 105)
    display.text("4.Supplying 3.3V to RPI Pico", 35, 135)
    sleep(5) 

def getReading(): 
    reading = sensor.read_u16()
    volts = reading * 3.3 / 65535
    print("Voltage:", volts)
    return volts 
    
def main():
    showMenu()
    reading = getReading()
    if (reading > 2.25) and (reading < 2.75): #test passed
        display.clear()
        display.text("Passed Manual Enable Test",88, 105)
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

