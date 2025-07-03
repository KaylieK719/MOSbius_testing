# Kaylie Kim
# June 30, 2025 
# File containing all the necessary helper functions that are used when running each test

## All necessary imports
from machine import ADC, Pin
from time import sleep, sleep_ms
from displayLCD import Display
import hardwareLCD
from ili9341 import color565

## Global pin connections
sensor = ADC(Pin(27)) #ADC GPIO 27
signal = Pin(1,Pin.OUT) #HI/LO output GPIO 1

## Connecting display
display = Display()

##Functions used in Power test
def powerTestMenu():
    """
        Displays directions for test & notifies user that test is running.
        (just writing text on the LCD)
        
        Takes no parameters
        
        Returns nothing 
        
    """
    display.clear()
    display.text("Testing power supply/supply protection:", 8,15)
    display.text("1.Place jumper on LDOO & V+",  35,  45)
    display.text("2.Connect LDOI to power supply", 35, 75)
    display.text("3.Supplying 3.3V to RPI Pico", 35, 105)
    sleep(5)
    
def getReading(): #MIGHT BE ABLE TO USE FOR GENERAL READINGSSS 
    """
        ADC reads voltage across power rail (breadboard) connected to the PCB.
        
        Parameters: None
        
        Returns volts (recalculated from reading to voltage)
        
    """
    reading = sensor.read_u16()
    volts = reading * 3.3 / 65535
    print("Voltage:", volts)
    return volts 

def runPowerTest():
    """
        Runs the PCB Power Test
        
        Displays pass/fail display and returns to main menu 
    """
    powerTestMenu()
    reading = getReading()
    if (reading > 2.25) and (reading < 2.75): #test passed
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


### Digital Level Shifter Tests
#Notes:
# - trying to figure out how to combine measureHI & measureLO functions
#   without having errors (doing it together seemed to produce errors in measurements)
# - TODO: combine DT CK EN tests 

def measureHI():
    """
        Reads DT,CK,EN pins when signal is HI
        
        Returns value in volts (converted from u16)
    """
    signal.value(1)
    reading1 = sensor.read_u16()
    sleep_ms(10)
    vHI = reading1 * 3.3 / 65535
    print(vHI)
    return vHI

def measureLO():
    """
        Reads DT,CK,EN pins when signal is LO
        
        Returns value in volts (converted from u16)
    """
    signal.value(0)
    sleep_ms(10)
    reading2 = sensor.read_u16()
    vLO = reading2 * 3.3 / 65535
    print(vLO)
    return vLO
        
def showMenuDT():
    """
        Displays directions for DT test
        
        Runs DT test
        
        Returns pass/fail
    """
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
    """
        Displays directions for CK test
        
        Runs CK
        
        Returns pass/fail
    """
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
    """
        Displays directions for EN test
        
        Runs EN
        
        Returns pass/fail
    """
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

def runDigitalLvlTest():
    """
        Runs the DT,CK,and EN (in this order) digital level shifter tests
        
        Returns pass/fail
    """ 
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

### Manual Enable Test
def manualENDirections():
    """
        Displays directions for manual enable test
    """
    display.clear()
    display.text("Testing manual enable:", 8,15)
    display.text("1.Place jumper on EM_PU",  35,  45)
    display.text("2.Connect LDOI to power supply", 35, 75)
    display.text("3.Place jumper on GPIO27 & EM pin", 35, 105)
    display.text("4.Supplying 3.3V to RPI Pico", 35, 135)
    sleep(5) 
    
def runManualENTest():
    """
        Runs manual enable test & makes sure the measured value is
        in an appropriate range
    """
    manualEnDirections()
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

def testPCB():
    """
        - Runs all tests for the PCB
    """
    runPowerTest()
    sleep(1)
    runDigitalLvlTest()
    sleep(1)
    runManualENTest()
    sleep(1)
    
### TESTS FOR CHIP (Note: These tests are manual)
options = ["YES", "NO"]
def yesNoMenu(highlight):
    for row, text in enumerate(options):
        y = 105 + row * 15            
        if row == highlight:
            display.fill_rect(0,y - 2,display.width,15,color565(255, 255, 255))
            display.text("> " + text, 136, y)
        else:
            display.text("> " + text, 136, y)
        
def nmosCurrBiasDirections():
    display.clear()
    display.text("Testing Current Bias Potentiometers:", 0,15)
    display.text("1.nMOS: connect ammeter to I_REFN",0,45)
    display.text("(bottom left)", 0,60) 
    display.text("- Do you measure ~10 micro Amps?", 0,75)
    
def runNmosCurrBiasTest():
    highlight = 0
    nmosCurrBiasDirections()
    yesNoMenu(highlight)
    while True:
        step = hardwareLCD.scrolling()    # –1, 0, or +1
        if step != 0:
            highlight = (highlight + step) % len(options)
            nmosCurrBiasDirections()
            yesNoMenu(highlight)
            sleep_ms(200)

        if hardwareLCD.isPressed():
            if options[highlight] == "YES":
                display.clear()
                display.text("Passed NMOS Curr Bias Test",0, 105)
                display.text("Launching PMOS Curr Bias Test", 0,120)
                for i in range(3):
                    display.text(".", 140+i*8, 135)
                    sleep(1)
                sleep(1)
                runPmosCurrBiasTest()
            else: #:NO
                display.clear()
                display.text("Test failed: Check connections", 40,105)
                display.text("Returning to menu", 88,120)
                for i in range(3):
                    display.text(".", 140+i*8, 135)
                    sleep(1)
                sleep(1)
                return
        sleep_ms(50)

def pmosCurrBiasDirections():
    display.clear()
    display.text("Testing Current Bias Potentiometers:", 0,15)
    display.text("1.pMOS: connect ammeter to I_REFP",0,45)
    display.text("(top middle)", 0,60) 
    display.text("- Do you measure ~10 micro Amps?", 0,75)   

    
def runPmosCurrBiasTest():
    highlight = 0
    pmosCurrBiasDirections()
    yesNoMenu(highlight)
    while True:
        step = hardwareLCD.scrolling()    # –1, 0, or +1
        if step != 0:
            highlight = (highlight + step) % len(options)
            nmosCurrBiasDirections()
            yesNoMenu(highlight)
            sleep_ms(200)

        if hardwareLCD.isPressed():
            if options[highlight] == "YES":
                display.clear()
                display.text("Passed PMOS Curr Bias Test",0, 105)
                display.text("Returning to Menu", 0,120)
                for i in range(3):
                    display.text(".", 140+i*8, 135)
                    sleep(1)
                sleep(1)
                return
            else: #:NO
                display.clear()
                display.text("Test failed: Check connections", 40,105)
                display.text("Returning to menu", 88,120)
                for i in range(3):
                    display.text(".", 140+i*8, 135)
                    sleep(1)
                sleep(1)
                return
        sleep_ms(50)


