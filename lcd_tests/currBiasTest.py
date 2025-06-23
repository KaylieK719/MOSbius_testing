from displayLCD import Display
import hardwareLCD
from ili9341 import color565
from time import sleep_ms, sleep

display = Display()

options = ["YES", "NO"]

def preDirections():
    display.clear()
    display.text("1.Verify socket is correctly soldered",0,15)
    display.text("  -Note: Pin 1 is in upper left corner",0,30)
    display.text("2.Insert MOSbius chip into socket", 0,60)
    display.text("  -Verify chip is seated properly", 0,75)
    sleep(5) 


def showMenuNMOS(highlight):
    display.clear()
    display.text("1.Connect ammeter to I_REFN",0,15)
    display.text(" -Does meter measure 10-100 micro amps?", 8,  30)
    display.text("2.Turn potentiometer & verify change",0, 60)
    display.text("  in current bias", 0,75)
    display.text(" -Set current bias to 100 micro amps",8, 90)

    for row, text in enumerate(options):
        y = 120 + row * 15            
        if row == highlight:
            display.fill_rect(0,y - 2,display.width,15,color565(255, 255, 255))
            display.text("> " + text, 136, y)
        else:
            display.text("> " + text, 136, y)
            
    while True:
            step = hardwareLCD.scrolling()    # –1, 0, or +1
            if step != 0:
                highlight = (highlight + step) % len(options)
                showMenuNMOS(highlight)
                sleep_ms(200)

            if hardwareLCD.isPressed():
                if options[highlight] == "YES":
                    return "NMOS Pass"
                else: #:NO
                    return "NMOS Fail"
                
def showMenuPMOS(highlight):
    display.clear()
    display.text("1.Connect ammeter to I_REFP",0,15)
    display.text(" -Does meter measure 10-100 micro amps?", 8,  30)
    display.text("2.Turn potentiometer & verify change",0, 60)
    display.text("  in current bias", 0,75)
    display.text(" -Set current bias to 100 micro amps",8, 90)

    for row, text in enumerate(options):
        y = 120 + row * 15            
        if row == highlight:
            display.fill_rect(0,y - 2,display.width,15,color565(255, 255, 255))
            display.text("> " + text, 136, y)
        else:
            display.text("> " + text, 136, y)
            
    while True:
            step = hardwareLCD.scrolling()    # –1, 0, or +1
            if step != 0:
                highlight = (highlight + step) % len(options)
                showMenuPMOS(highlight)
                sleep_ms(200)

            if hardwareLCD.isPressed():
                if options[highlight] == "YES":
                    return "PMOS Pass"
                else: #:NO
                    return "PMOS Fail"


def main():
    highlight = 0
    preDirections()
    currStatus = showMenuNMOS(highlight)
    
    if currStatus == "NMOS Pass": #NMOS test passed
        display.clear()
        display.text("Passed NMOS current bias",64, 90)
        display.text("potentiometer test",88,105)
        display.text("Running PMOS test", 92,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1)
        currStatus = showMenuPMOS(highlight)
    
    if currStatus == "NMOS Fail": #NMOS test failed
        display.clear()
        display.text("Test failed: Check connections", 40,105)
        display.text("Returning to menu", 88,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1)
        return
    
    if currStatus == "PMOS Pass": #PMOS test passed
        display.clear()
        display.text("Passed PMOS current bias",64, 90)
        display.text("potentiometer test",88,105)
        display.text("Returning to menu", 88,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1)
        return 
    
    if currStatus == "PMOS Fail": #PMOS test failed
        display.clear()
        display.text("Test failed: Check connections", 40,105)
        display.text("Returning to menu", 88,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1)
        return
    
main()
