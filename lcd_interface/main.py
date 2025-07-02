# Main.py V2
- Combined logic for each menu and submenu screen to one function 
- Implements menu and submenu interface 
- New BACK button to switch between menus
- Implements new helperFunctions module (contains all test functions)

#Menu imports 
import hardwareLCD
from displayLCD import Display
import helperFunctions
from ili9341 import color565 #Display import 
from newMenu import Menu
from runnerLCD  import launch
from time import sleep_ms
#ADC/Pin Imports 
from machine import ADC, Pin

tests = {
    "Power Test": helperFunctions.runPowerTest,
    "Digital Level Shifter Test": helperFunctions.runDigitalLvlTest,
    "DT digitalLvl Test": helperFunctions.showMenuDT,
    "CK digitalLvl Test": helperFunctions.showMenuCK,
    "EN digitalLvl Test": helperFunctions.showMenuEN,
    "Manual Enable Test": helperFunctions.runManualENTest
    "Test PCB": helperFunctions.testPCB
    }

def main():
    """
        1. Initializes display, menu, and draws the main menu
        Note: menu.files changes based on current menu
        2. Checks for scrolling ^ or v
        3. Pressed button switches between each menu and submenu screen
        4. Launches desired test to be carried out
    """
    display = Display()
    menu = Menu(display)
    menu.drawMenu(menu.files)

    while True:
        step = hardwareLCD.scrolling()
        if step != 0:
            menu.moveCursor(step)

        #Deals with switching between menus 
        if hardwareLCD.isPressed():
            if menu.files[menu.step] == "Test PCB":
                menu.files = menu.PCBTests
            elif menu.files[menu.step] == "Test Chip":
                menu.files = menu.chipTests
            elif menu.files[menu.step] == "BACK":
                print("this part works")
                menu.files = menu.mainMenuTests
            else:
                function = menu.files[menu.step]
                print("Launching:", function)
                launch(display, function,tests[function])
                
            menu.drawMenu(menu.files)

        sleep_ms(10)

if __name__ == "__main__":
    main()

