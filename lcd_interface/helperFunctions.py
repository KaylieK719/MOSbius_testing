# Kaylie Kim
# July 15, 2025 
# File containing all the necessary helper functions that are used when running each test
# Added & fixed functions for tests 

## All necessary imports
from machine import ADC, Pin
from time import sleep, sleep_ms
from ili9341 import color565
from programChip import program
import interface

## Global pin connections
sensor = ADC(Pin(27)) #ADC GPIO 27
signal = Pin(1,Pin.OUT) #HI/LO output GPIO 1

## Miscellaneous Functions 
options = ["YES", "NO"]
def yesNoMenu(highlight,display):
    """
        Menu option (yes or no) display menu
    """
    for row, text in enumerate(options):
        y = 120 + row * 15            
        if row == highlight:
            display.fill_rect(0,y - 2,display.width,15,color565(255, 255, 255))
            display.text("> " + text, 136, y)
        else:
            display.text("> " + text, 136, y)
            
def loading(display):
    """
        Short delay before test starts
    """
    for i in range(3):
        display.text(".", 96+i*8, 135)
        sleep(1)

##Functions used in Power test
def powerTestMenu(display):
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

def runPowerTest(display):
    """
        Runs the PCB Power Test
        
        Displays pass/fail display and returns to main menu 
    """
    powerTestMenu(display)
    reading = getReading()
    if (reading > 2.25) and (reading < 2.75): #test passed
        display.clear()
        display.text("Passed Power Test",88, 105)
        display.text("Returning to menu", 88,120)
        loading(display) 
        return
    
    else:
        display.clear()
        display.text("Test failed: Check connections", 40,105)
        display.text("Returning to menu", 88,120)
        loading(display)
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
        
def showMenuDT(display):
    """
        Displays directions for DT test
        
        Runs DT test
        
        Returns pass/fail
    """
    display.clear()
    display.text("-Place jumper GPIO27 to DT",0,15)
    display.text("-Place jumper GPIO1 to DT(top)",0,45)
    display.text("Measuring high & low voltage", 0,75)
    loading(display)
    vHI = measureHI()
    vLO = measureLO()

    if ((vHI > 2.25) and (vHI < 2.75)
        and (vLO > 0.0000) and (vLO < 0.25)):
        display.clear()
        display.text("Passed data level test",72, 105)
        display.text("Running clock level test", 64,120)
        loading(display)
        return "DT Pass"
    else:
        display.clear()
        display.text("Test failed: Check connections",0,105)
        display.text("Returning to menu", 52,120)
        loading(display)
        return "DT Fail"
    

def showMenuCK(display):
    """
        Displays directions for CK test
        
        Runs CK
        
        Returns pass/fail
    """
    display.clear()
    display.text("-Place jumper GPIO27 to CK",0,15)
    display.text("-Place jumper GPIO1 to CK(top)",0,45)
    display.text("Measuring high & low voltage", 0, 75)
    loading(display)
    vHI = measureHI()
    vLO = measureLO()

    if ((vHI > 2.25) and (vHI < 2.75) and (vLO > 0) and (vLO < 0.25)):
        display.clear()
        display.text("Passed clock level test",68, 105)
        display.text("Running enable level test", 60,120)
        loading(display)
        return "CK Pass"
    else:
        display.clear()
        display.text("Test failed: Check connections", 40,105)
        display.text("Returning to menu", 52,120)
        loading(display)
        return "CK Fail"

def showMenuEN(display):
    """
        Displays directions for EN test
        
        Runs EN
        
        Returns pass/fail
    """
    display.clear()
    display.text("-Place jumper GPIO27 to EN",0,15)
    display.text("-Place jumper GPIO1 to EN(top)",0,45)
    display.text("Measuring high & low voltage", 0, 75)
    loading(display)
    vHI = measureHI()
    vLO = measureLO()

    if ((vHI > 2.25) and (vHI < 2.75)
        and (vLO > 0) and (vLO < 0.25)):
        display.clear()
        display.text("Passed enable level test",68, 105)
        display.text("Returning to menu", 52,120)
        loading(display)
        return "EN Pass"
    else:
        display.clear()
        display.text("Test failed: Check connections", 40,105)
        display.text("Returning to menu", 52,120)
        loading(display)
        return "EN Fail"

def runDigitalLvlTest(display):
    """
        Runs the DT,CK,and EN (in this order) digital level shifter tests
        
        Returns pass/fail
    """ 
    currStatus = showMenuDT(display)
    
    if currStatus == "DT Pass": #DT test passed
        currStatus = showMenuCK(display)
    
    if currStatus == "DT Fail": #DT test failed 
        return
        
    if currStatus == "CK Pass": #Passed CK test
        currStatus = showMenuEN(display)
        
    if currStatus == "CK Fail": #CK test failed 
        return
    
    if currStatus == "EN Pass": #Passed EN test
        return
    
    else: #EN test failed
        return  

### Manual Enable Test
def manualENDirections(display):
    """
        Displays directions for manual enable test
    """
    display.clear()
    display.text("Testing manual enable:", 0,15)
    display.text("-Place jumper on EM_PU", 0,  45) 
    display.text("-Connect LDOI to power supply", 0, 75)
    display.text("-Place jumper on GPIO27 & EM", 0, 105)
    display.text("-Supplying 3.3V to RPI Pico", 0, 135)
    sleep(5) 
    
def runManualENTest(display):
    """
        Runs manual enable test & makes sure the measured value is
        in an appropriate range
    """
    manualENDirections(display)
    reading = getReading()
    if (reading > 2.25) and (reading < 2.75): #test passed
        display.clear()
        display.text("Passed Manual Enable Test",0, 105)
        display.text("Returning to menu", 88,120)
        loading(display)
        return
    
    else:
        display.clear()
        display.text("Test failed: Check connections", 0,105)
        display.text("Returning to menu", 88,120)
        loading(display)
        return 

def testPCB(display):
    """
        - Runs all tests for the PCB
    """
    runPowerTest(display)
    sleep(1)
    runDigitalLvlTest(display)
    sleep(1)
    runManualENTest(display)
    sleep(1)
    
### TESTS FOR CHIP (Note: These tests are manual
        
def nmosCurrBiasDirections(display):
    display.clear()
    display.text("Testing Curr Bias (nmos)", 0,15)
    display.text("1.connect ammeter to I_REFN",0,45)
    display.text("Confirm ~10 micro Amps;", 0,75)
    
def runNmosCurrBiasTest(display,hardware):
    """
        Current Bias test for NMOS
        if passed, runs Current Bias test for PMOS
    """
    highlight = 0
    nmosCurrBiasDirections(display)
    yesNoMenu(highlight,display)
    while True:
        step = hardware.scrolling()    # –1, 0, or +1
        if step != 0:
            highlight = (highlight + step) % len(options)
            nmosCurrBiasDirections(display)
            yesNoMenu(highlight,display)
            sleep_ms(200)

        if hardware.isPressed():
            if options[highlight] == "YES":
                display.clear()
                display.text("Passed NMOS Curr Bias Test",0, 105)
                display.text("Launching PMOS Curr Bias Test", 0,120)
                loading(display)
                runPmosCurrBiasTest(display,hardware)
                return
            else: #:NO
                display.clear()
                display.text("Test failed: Check connections", 40,105)
                display.text("Returning to menu", 88,120)
                loading(display)
                return
        sleep_ms(50)

def pmosCurrBiasDirections(display):
    display.clear()
    display.text("Testing Curr Bias (pmos)", 0,15)
    display.text("1.connect ammeter to I_REFP",0,45)
    display.text("Confirm ~10 micro Amps;", 0,75)

    
def runPmosCurrBiasTest(display,hardware):
    """
        Current Bias test for PMOS
        if passed Current Bias test is passed
    """
    highlight = 0
    pmosCurrBiasDirections(display)
    yesNoMenu(highlight,display)
    while True:
        step = hardware.scrolling()    # –1, 0, or +1
        if step != 0:
            highlight = (highlight + step) % len(options)
            yesNoMenu(highlight,display)
            sleep_ms(200)

        if hardware.isPressed():
            if options[highlight] == "YES":
                display.clear()
                display.text("Passed PMOS Curr Bias Test",0, 105)
                display.text("Returning to Menu", 0,120)
                loading(display)
                return
            else: #:NO
                display.clear()
                display.text("Test failed: Check connections", 40,105)
                display.text("Returning to menu", 88,120)
                loading(display)
                return
        
def threeRODirections(display):
    display.clear()
    display.text("Testing 3 Ring Oscillator:", 0,15)
    display.text("-Programming Chip",0,45)
    display.text("-Place scope at STAGE1,2,3",0,60)
    display.text("-Confirm for correct waveforms", 0,90)
    
def runThreeROTest(display,hardware):
    """
        Programs the chip for a 16-16-8 ring oscillator
        Prompts user to check for correct waveform on oscilloscope to pass
        Asks to check waveform for stage 1,2,3
    """ 
    highlight = 0
    threeRODirections(display)
    program()
    yesNoMenu(highlight,display)
    while True:
        step = hardware.scrolling()    # –1, 0, or +1
        if step != 0:
            highlight = (highlight + step) % len(options)
            threeRODirections(display)
            yesNoMenu(highlight,display)
            sleep_ms(10)

        if hardware.isPressed():
            if options[highlight] == "YES":
                display.clear()
                display.text("Passed 3 Ring Oscillator Test",0, 105)
                display.text("Returning to Menu", 0,120)
                loading(display)
                return
            else: #:NO
                display.clear()
                display.text("Test failed: Check connections", 40,105)
                display.text("Returning to menu", 88,120)
                loading(display)
                return
        sleep_ms(50)

