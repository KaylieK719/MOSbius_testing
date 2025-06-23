from displayLCD import Display
import hardwareLCD
from ili9341 import color565
from time import sleep_ms, sleep

display = Display()

options = ["YES", "NO"]

def showMenuDT(highlight):
    display.clear()
    display.text("Connect oscilloscope probe to DT header",0,0)
    display.text("Applying 3.3V square wave",  35,  30)
    display.text("1.Is blue LED blinking?", 35, 45)
    display.text("2.Does scope read 2.5V signal?", 35, 60)

    for row, text in enumerate(options):
        y = 105 + row * 15            
        if row == highlight:
            display.fill_rect(0,y - 2,display.width,15,color565(255, 255, 255))
            display.text("> " + text, 136, y)
        else:
            display.text("> " + text, 136, y)
            
    #dtMenuLoop
    while True:
            step = hardwareLCD.scrolling()    # –1, 0, or +1
            if step != 0:
                highlight = (highlight + step) % len(options)
                showMenuDT(highlight)
                sleep_ms(200)

            if hardwareLCD.isPressed():
                if options[highlight] == "YES":
                    return "CK"
                else: #:NO
                    return "DT Fail"

def showMenuCK(highlight):
    display.clear()
    display.text("Connect oscilloscope probe to CK header",0,0)
    display.text("Applying 3.3V square wave",  35,  30)
    display.text("1.Is yellow LED blinking?", 35, 45)
    display.text("2.Does scope read 2.5V signal?", 35, 60)

    for row, text in enumerate(options):
        y = 105 + row * 15            
        if row == highlight:
            display.fill_rect(0,y - 2,display.width,15,color565(255, 255, 255))
            display.text("> " + text, 136, y)
        else:
            display.text("> " + text, 136, y)
            
     #ckMenuLoop
    while True:
            step = hardwareLCD.scrolling()    # –1, 0, or +1
            if step != 0:
                highlight = (highlight + step) % len(options)
                showMenuCK(highlight)
                sleep_ms(200)

            if hardwareLCD.isPressed():
                if options[highlight] == "YES":
                    return "EN"
                else: #:NO
                    return "CK Fail"

def showMenuEN(highlight):
    display.clear()
    display.text("Connect oscilloscope probe to EN header",0,0)
    display.text("Applying 3.3V square wave",  35,  30)
    display.text("1.Is green LED blinking?", 35, 45)
    display.text("2.Does scope read 2.5V signal?", 35, 60)

    for row, text in enumerate(options):
        y = 105 + row * 15            
        if row == highlight:
            display.fill_rect(0,y - 2,display.width,15,color565(255, 255, 255))
            display.text("> " + text, 136, y)
        else:
            display.text("> " + text, 136, y)
            
     #enMenuLoop
    while True:
            step = hardwareLCD.scrolling()    # –1, 0, or +1
            if step != 0:
                highlight = (highlight + step) % len(options)
                showMenuEN(highlight)
                sleep_ms(200)

            if hardwareLCD.isPressed():
                if options[highlight] == "YES":
                    return "EN Passed"
                else: #:NO
                    return "EN Failed"

def main():
    highlight = 0
    currStatus = showMenuDT(highlight)
    
    if currStatus == "CK": #DT test passed
        display.clear()
        display.text("Passed data level test",72, 105)
        display.text("Running clock level test", 64,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1)
        currStatus = showMenuCK(highlight)
    
    if currStatus == "DT Fail": #DT test failed
        display.clear()
        display.text("Test failed: Check connections", 40,105)
        display.text("Returning to menu", 88,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1)
        return
        
    if currStatus == "EN": #Passed CK test
        display.clear()
        display.text("Passed clock level test",68, 105)
        display.text("Running enable level test", 60,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1)
        currStatus = showMenuEN(highlight)
        
    if currStatus == "CK Fail": #CK test failed 
        display.clear()
        display.text("Test failed: Check connections", 40,105)
        display.text("Returning to menu", 88,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1)
        return
    
    if currStatus == "EN Passed": #Passed EN test
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
