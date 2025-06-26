#Three-Stage Ring Oscillator (16-16-8)
from displayLCD import Display
import hardwareLCD
from ili9341 import color565
from time import sleep_ms, sleep

display = Display()

options = ["YES", "NO"]

def directions():
    display.clear()
    display.text("Part 1: Setup", 0,0)
    
    display.text("1.Connect from RPI Pico to pins (top)",0,15)
    display.text("  GPIO 10 --> EN", 0,30)
    display.text("  GPIO 11 --> CK", 0,45)
    display.text("  GPIO 12 --> DT", 0,60)
    
    display.text("2.Connect +1 +2 on ADALM to pins (left)", 0,90)
    display.text("3.Connect CH1 --> stage1 output", 0, 120)
    display.text("  Connect CH2 --> stage2 output", 0,135)
    
    display.text("Part 2:Run main.py & scope to start test", 0,165)
    sleep(5)


def stageOne(highlight):
    display.clear()
    display.text("Stage 1:", 0,30)
    display.text(" - Do scopes read 12.8-15.62 MHz?", 0,45)
    display.text(" - Is peak-to-peak ---?",0,75)
    
    for row, text in enumerate(options):
        y = 105 + row * 15            
        if row == highlight:
            display.fill_rect(0,y - 2,display.width,15,color565(255, 255, 255))
            display.text("> " + text, 136, y)
        else:
            display.text("> " + text, 136, y)
            
    while True:
            step = hardwareLCD.scrolling()    # –1, 0, or +1
            if step != 0:
                highlight = (highlight + step) % len(options)
                showMenuDT(highlight)
                sleep_ms(200)

            if hardwareLCD.isPressed():
                if options[highlight] == "YES": 
                    return "STAGE ONE PASS"
                else: #:NO
                    return "STAGE ONE FAIL"
                
def stageTwo(highlight):
    display.clear()
    display.text("Stage 2:", 0,30)
    display.text(" - Do scopes read --- MHz?", 0,45)
    display.text(" - Is peak-to-peak ---?",0,75) 
    
    for row, text in enumerate(options):
        y = 105 + row * 15            
        if row == highlight:
            display.fill_rect(0,y - 2,display.width,15,color565(255, 255, 255))
            display.text("> " + text, 136, y)
        else:
            display.text("> " + text, 136, y)
            
    while True:
            step = hardwareLCD.scrolling()    # –1, 0, or +1
            if step != 0:
                highlight = (highlight + step) % len(options)
                showMenuDT(highlight)
                sleep_ms(200)

            if hardwareLCD.isPressed():
                if options[highlight] == "YES": 
                    return "STAGE TWO PASS"
                else: #:NO
                    return "STAGE TWO FAIL"
                
def stageThree(highlight):
    display.clear()
    display.text("Stage 3:", 0,30)
    display.text(" - Do scopes read --- MHz?", 0,45)
    display.text(" - Is peak-to-peak ---?",0,75) 
    
    for row, text in enumerate(options):
        y = 105 + row * 15            
        if row == highlight:
            display.fill_rect(0,y - 2,display.width,15,color565(255, 255, 255))
            display.text("> " + text, 136, y)
        else:
            display.text("> " + text, 136, y)
            
    while True:
            step = hardwareLCD.scrolling()    # –1, 0, or +1
            if step != 0:
                highlight = (highlight + step) % len(options)
                showMenuDT(highlight)
                sleep_ms(200)

            if hardwareLCD.isPressed():
                if options[highlight] == "YES": 
                    return "STAGE THREE PASS"
                else: #:NO
                    return "STAGE THREE FAIL"

def main():
    highlight = 0
    directions()
    currStatus = stageOne(highlight)
    
    if currStatus == "STAGE ONE PASS":
        display.clear()
        display.text("Stage one pass", 104,105)
        display.text("Testing stage two",92, 120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1)
        currStatus = stageTwo(highlight)
        
    if currStatus == "STAGE ONE FAIL":
        display.clear()
        display.text("Test failed: Check connections", 40,105)
        display.text("Returning to menu", 88,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1) 
        return
    
    if currStatus == "STAGE TWO PASS":
        display.clear()
        display.text("Stage two pass",104, 105)
        display.text("Testing stage three",84,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1)
        currStatus = stageThree(highlight)
            
    if currStatus == "STAGE TWO FAIL": 
        display.clear()
        display.text("Test failed: Check connections", 40,105)
        display.text("Returning to menu", 88,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1)
        return
        
    if currStatus == "STAGE THREE PASS":
        display.clear()
        display.text("Passed 3-Stage Oscillator Test",40, 105)
        display.text("Returning to menu", 88,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1)
        return
    
    else:
        display.clear()
        display.text("Test failed: Check connections", 40,105)
        display.text("Returning to menu", 88,120)
        for i in range(3):
            display.text(".", 140+i*8, 135)
            sleep(1)
        sleep(1)
        return  

main()


