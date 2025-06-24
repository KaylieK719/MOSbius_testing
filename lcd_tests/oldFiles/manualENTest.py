from displayLCD import Display
import hardwareLCD
from ili9341 import color565
from time import sleep_ms, sleep

display = Display()

options = ["YES", "NO"]

def showMenu(highlight):
    display.clear()
    display.text("1.Place jumper on EM_PU",  68,  30)
    display.text("2.Supply 2.5V to RPI Pico", 60, 45)
    display.text("Is orange EN_MAN LED on?", 64, 60)

    for row, text in enumerate(options):
        y = 105 + row * 15            
        if row == highlight:
            display.fill_rect(0,y - 2,display.width,15,color565(255, 255, 255))
            display.text("> " + text, 136, y)
        else:
            display.text("> " + text, 136, y)

def main():

    highlight = 0
    showMenu(highlight)

    while True:
        step = hardwareLCD.scrolling()    # –1, 0, or +1
        if step != 0:
            highlight = (highlight + step) % len(options)
            showMenu(highlight)
            sleep_ms(200)

        if hardwareLCD.isPressed():
            if options[highlight] == "YES":
                display.clear()
                display.text("Passed Manual Enable Test",60, 105)
                display.text("Returning to menu", 88,120)
                for i in range(3):
                    display.text(".", 140+i*8, 135)
                    sleep(1)
                break
                print("Ran break")
            
            else: #:NO
                display.clear()
                display.text("Test failed: Check connections", 40,105)
                display.text("Returning to menu", 88,120)
                for i in range(3):
                    display.text(".", 140+i*8, 135)
                    sleep(1)
                break
        sleep_ms(50)

main()



