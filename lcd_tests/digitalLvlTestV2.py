from displayLCD import Display
import hardwareLCD
from ili9341 import color565
from time import sleep_ms, sleep
from machine import Pin, ADC

display = Display()

signal = Pin(1,Pin.OUT) #GPIO Pin 1 for HI/LO output 
sensor = ADC(Pin(27)) #ADC GPIO 27

def measureHI():
    signal.value(1)
    reading1 = sensor.read_u16()
    sleep_ms(10)
    vHI = reading1 * 3.3 / 65535
    print(vHI)
    return vHI

def measureLO():
    signal.value(0)
    sleep_ms(10)
    reading2 = sensor.read_u16()
    vLO = reading2 * 3.3 / 65535
    print(vLO)
    return vLO
        
def showMenuDT():
    display.clear()
    display.text("-Place jumper from GPIO27 to DT pin",0,15)
    display.text("-Place jumper from GPIO1 to DT pin (top)",0,45)
    display.text("Measuring high & low voltage", 48,75)
    for i in range(3):
        display.text(".", 140+i*8, 105)
        sleep(1)
    sleep(1)
    vHI = measureHI()
    vLO = measureLO()

    if ((vHI > 2.25) and (vHI < 2.75)
        and (vLO > 0.0000) and (vLO < 0.25)):
        return "DT Pass"
    else:
        return "DT Fail"
    

def showMenuCK():
    display.clear()
    display.text("-Place jumper from GPIO27 to CK pin",0,15)
    display.text("-Place jumper from GPIO1 to CK pin (top)",0,45)
    display.text("Measuring high & low voltage", 48, 75)
    for i in range(3):
        display.text(".", 140+i*8, 105)
        sleep(1)
    sleep(1)
    vHI = measureHI()
    vLO = measureLO()

    if ((vHI > 2.25) and (vHI < 2.75) and (vLO > 0) and (vLO < 0.25)):
        return "CK Pass"
    else:
        return "CK Fail"

def showMenuEN():
    display.clear()
    display.text("-Place jumper from GPIO27 to EN pin",0,15)
    display.text("-Place jumper from GPIO1 to EN pin (top)",0,45)
    display.text("Measuring high & low voltage", 48, 75)
    for i in range(3):
        display.text(".", 140+i*8, 105)
        sleep(1)   
    sleep(1)
    vHI = measureHI()
    vLO = measureLO()

    if ((vHI > 2.25) and (vHI < 2.75)
        and (vLO > 0) and (vLO < 0.25)):
        return "EN Pass"
    else:
        return "EN Fail"

def main():
    currStatus = showMenuDT()
    
    if currStatus == "DT Pass": #DT test passed
        display.clear()
        display.text("Passed data level test",72, 105)
        display.text("Running clock level test", 64,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1)
        currStatus = showMenuCK()
    
    if currStatus == "DT Fail": #DT test failed
        display.clear()
        display.text("Test failed: Check connections", 40,105)
        display.text("Returning to menu", 88,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1) 
        return
        
    if currStatus == "CK Pass": #Passed CK test
        display.clear()
        display.text("Passed clock level test",68, 105)
        display.text("Running enable level test", 60,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1)
        currStatus = showMenuEN()
        
    if currStatus == "CK Fail": #CK test failed 
        display.clear()
        display.text("Test failed: Check connections", 40,105)
        display.text("Returning to menu", 88,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1)
        return
    
    if currStatus == "EN Pass": #Passed EN test
        display.clear()
        display.text("Passed enable level test",68, 105)
        display.text("Returning to menu", 88,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1)
        return
    
    else: #EN test failed
        display.clear()
        display.text("Test failed: Check connections", 40,105)
        display.text("Returning to menu", 88,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1)
        return  

main()
