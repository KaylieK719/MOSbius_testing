#INCOMPLETE STILL IN PROGRESS
from displayLCD import Display
import hardwareLCD
from ili9341 import color565
from time import sleep_ms, sleep

display = Display()

options = ["YES", "NO"]

def showMenuDT(highlight):
    display.clear()
    display.text("Connect oscilloscope probe to DT header"0,0)
    display.text("Applying 3.3V square wave",  35,  30)
    display.text("1.Is blue LED blinking?", 35, 45)
    display.text("2.Does oscilloscope read 2.5V signal?", 35, 60)

    for row, text in enumerate(options):
        y = 105 + row * 15            
        if row == highlight:
            display.fill_rect(0,y - 2,display.width,15,color565(255, 255, 255))
            display.text("> " + text, 136, y)
        else:
            display.text("> " + text, 136, y)

def showMenuCK(highlight):
    display.clear()
    display.text("Connect oscilloscope probe to CK header"0,0)
    display.text("Applying 3.3V square wave",  35,  30)
    display.text("1.Is yellow LED blinking?", 35, 45)
    display.text("2.Does oscilloscope read 2.5V signal?", 35, 60)

    for row, text in enumerate(options):
        y = 105 + row * 15            
        if row == highlight:
            display.fill_rect(0,y - 2,display.width,15,color565(255, 255, 255))
            display.text("> " + text, 136, y)
        else:
            display.text("> " + text, 136, y)

def showMenuEN(highlight):
    display.clear()
    display.text("Connect oscilloscope probe to EN header"0,0)
    display.text("Applying 3.3V square wave",  35,  30)
    display.text("1.Is green LED blinking?", 35, 45)
    display.text("2.Does oscilloscope read 2.5V signal?", 35, 60)

    for row, text in enumerate(options):
        y = 105 + row * 15            
        if row == highlight:
            display.fill_rect(0,y - 2,display.width,15,color565(255, 255, 255))
            display.text("> " + text, 136, y)
        else:
            display.text("> " + text, 136, y)
   
def runningTest(currTest):
        while True:
        step = hardwareLCD.scrolling()    # –1, 0, or +1
        if step != 0:
            highlight = (highlight + step) % len(options)
            showMenu(highlight)
            sleep_ms(200)

        if hardwareLCD.isPressed():
            if options[highlight] == "YES":
                display.clear()
                display.text("Passed Power Test",88, 105)
                display.text("Returning to menu", 88,120)
                for i in range(3):
                    display.text(".", 140+i*8, 135)
                    sleep(1)
                sleep(1)
                break
            else: #:NO
                display.clear()
                display.text("Test failed: Check connections", 40,105)
                display.text("Returning to menu", 88,120)
                for i in range(3):
                    display.text(".", 140+i*8, 135)
                    sleep(1)
                sleep(1)
                break
        sleep_ms(50)
   
def main():
    tests = {
        dtTest:True,
        ckTest:False,
        enTest: False
        }

    highlight = 0
    
    showMenuDT(highlight)



main()



