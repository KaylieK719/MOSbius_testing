# Kaylie Kim
# July 23, 2025 
# helperFunctions V5 
# Addresses small bugs & timing of tests for efficiency 

from machine import ADC, Pin
from time import sleep, sleep_ms
from ili9341 import color565
from programChip import program,PIN_EN,PIN_CLK, PIN_DATA
import interface

## Global pin connections
sensorO = ADC(Pin(27)) #ORANGE 
sensorG = ADC(Pin(26)) #GREEN
sensorY = ADC(Pin(28)) #YELLOW

en  = Pin(PIN_EN,  Pin.OUT, value=0)
clk = Pin(PIN_CLK, Pin.OUT)
dt  = Pin(PIN_DATA,Pin.OUT)

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
            display.text("> " + text, 100, y)
        else:
            display.text("> " + text, 100, y)
        
def sleepMenu():
    sleep(3)

##Functions used in Power test
def powerTestMenu(display):
    """
        Displays directions for test & notifies user that test is running.
        (just writing text on the LCD)
        
        Takes no parameters
        
        Returns nothing 
        
    """
    display.clear()
    display.text("Testing power supply:", 0,15)
    display.text("1.Place jumper on LDOO & V+",  0 ,45)
    display.text("2.Connect LDOI to power supply", 0, 75)
    display.text("3.Supplying 3.3V to RPI Pico", 0, 105)
    sleepMenu()
    
def getReading(): #MIGHT BE ABLE TO USE FOR GENERAL READINGSSS 
    """
        ADC reads voltage across power rail (breadboard) connected to the PCB.
        
        Parameters: None
        
        Returns volts (recalculated from reading to voltage)
        
    """
    reading = sensorO.read_u16()
    volts = reading * 3.3 / 65535
    print("Voltage:", volts)
    return volts 

def runPowerTest(display,hardware):
    """
        Runs the PCB Power Test
        
        Displays pass/fail display and returns to main menu 
    """
    powerTestMenu(display)
    reading = getReading()
    if (reading > 2.25) and (reading < 2.75): #test passed
        display.clear()
        display.text("Passed Power Test",0, 15)
        display.text(f"measured: {reading}V", 0,45)
        display.text("Returning to menu...", 0,75)
        sleepMenu()
        return
    
    else:
        display.clear()
        display.text("Test failed:Check connections", 0,15)
        display.text(f"measured: {reading}V", 0,45)
        display.text("Returning to menu...", 0,75)
        sleepMenu()
        return
    


### Digital Level Shifter Tests
def measureHI(pin,sensor):
    """
        Reads DT,CK,EN pins when signal is HI
        
        Returns value in volts (converted from u16)
    """
    pin.value(1)
    reading1 = sensor.read_u16()
    sleep_ms(10)
    vHI = reading1 * 3.3 / 65535
    print(vHI)
    return vHI

def measureLO(pin,sensor):
    """
        Reads DT,CK,EN pins when signal is LO
        
        Returns value in volts (converted from u16)
    """
    pin.value(0)
    sleep_ms(10)
    reading2 = sensor.read_u16()
    vLO = reading2 * 3.3 / 65535
    print(vLO)
    return vLO
        
def showMenuDT(display,hardware):
    """
        Displays directions for DT test
        
        Runs DT test
        
        Returns pass/fail
    """
    display.clear()
    display.text("Testing DT Lvl Shifter:", 0,15)
    display.text("-Place YELLOW wire to DT",0,45)
    display.text("-Place wire to DT(top)",0,75)
    display.text("Measuring high & low voltage:", 0,105)
    sleepMenu() 
    vHI = measureHI(dt,sensorY)
    vLO = measureLO(dt,sensorY)

    if ((vHI > 2.25) and (vHI < 2.75)
        and (vLO > 0.0000) and (vLO < 0.25)):
        display.clear()
        display.text("Passed data level test",0, 15)
        display.text(f"vHI = {vHI}",0,45)
        display.text(f"vLO = {vLO}", 0,75)
        display.text("Returning to menu...", 0,105)
        sleepMenu()
        return "DT Pass"
    else:
        display.clear()
        display.text("Test failed:Check connections",0,15)
        display.text(f"vHI = {vHI}",0,45)
        display.text(f"vLO = {vLO}", 0,75)
        display.text("Returning to menu...", 0,105)
        sleepMenu()
        return "DT Fail"
    

def showMenuCK(display,hardware):
    """
        Displays directions for CK test
        
        Runs CK
        
        Returns pass/fail
    """
    display.clear()
    display.text("Testing CK Lvl Shifter:", 0,15)
    display.text("-Place GREEN wire to CK",0,45)
    display.text("-Place wire to CK(top)",0,75)
    display.text("Measuring high & low voltage", 0,105)
    sleepMenu()
    vHI = measureHI(clk,sensorG)
    vLO = measureLO(clk,sensorG)

    if ((vHI > 2.25) and (vHI < 2.75) and (vLO > 0) and (vLO < 0.25)):
        display.clear()
        display.text("Passed clock level test",0, 15)
        display.text(f"vHI = {vHI}",0,45)
        display.text(f"vLO = {vLO}", 0,75)
        display.text("Returning to menu...", 0,105)
        sleepMenu()
        return "CK Pass"
    else:
        display.clear()
        display.text("Test failed:Check connections", 0,15)
        display.text(f"vHI = {vHI}",0,45)
        display.text(f"vLO = {vLO}", 0,75)
        display.text("Returning to menu...", 0,105)
        sleepMenu()
        return "CK Fail"

def showMenuEN(display,hardware):
    """
        Displays directions for EN test
        
        Runs EN
        
        Returns pass/fail
    """
    display.clear()
    display.text("Testing EN Lvl Shifter:" ,0,15)
    display.text("-Place ORANGE wire to EN",0,45)
    display.text("-Place jumper to EN(top)",0,75)
    display.text("Measuring high & low voltage", 0, 105)
    sleepMenu()
    vHI = measureHI(en,sensorO)
    vLO = measureLO(en,sensorO)

    if ((vHI > 2.25) and (vHI < 2.75)
        and (vLO > 0) and (vLO < 0.25)):
        display.clear()
        display.text("Passed enable level test",0, 15)
        display.text(f"vHI = {vHI}",0,45)
        display.text(f"vLO = {vLO}", 0,75)
        display.text("Returning to menu...", 0,105)
        sleepMenu()
        return "EN Pass"
    else:
        display.clear()
        display.text("Test failed:Check connections", 0,15)
        display.text(f"vHI = {vHI}",0,45)
        display.text(f"vLO = {vLO}", 0,75)
        display.text("Returning to menu...", 0,105)
        sleepMenu()
        return "EN Fail"

def runDigitalLvlTest(display,hardware):
    """
        Runs the DT,CK,and EN (in this order) digital level shifter tests
        
        Returns pass/fail
    """ 
    currStatus = showMenuDT(display,hardware)
    
    if currStatus == "DT Pass": #DT test passed
        currStatus = showMenuCK(display,hardware)
    
    if currStatus == "DT Fail": #DT test failed 
        return
        
    if currStatus == "CK Pass": #Passed CK test
        currStatus = showMenuEN(display,hardware)
        
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
    display.text("-Place ORANGE jumper to EM", 0, 105)
    display.text("-Supplying 3.3V to RPI Pico", 0, 135)
    sleepMenu()
    
def runManualENTest(display,hardware):
    """
        Runs manual enable test & makes sure the measured value is
        in an appropriate range
    """
    manualENDirections(display)
    reading = getReading()
    if (reading > 2.25) and (reading < 2.75): #test passed
        display.clear()
        display.text("Passed Manual Enable Test",0, 15)
        display.text(f"reading = {reading}",0,45)
        display.text("Remove jumper from EM_PU", 0,75)
        display.text("Returning to menu...", 0,105)
        sleepMenu()
        return
    
    else:
        display.clear()
        display.text("Test failed:Check connections", 0,15)
        display.text(f"reading = {reading}",0,45)
        display.text("Returning to menu", 0,75)
        sleepMenu()
        return 
    
### TESTS FOR CHIP (Note: These tests are manual
        
def nmosCurrBiasDirections(display):
    """
        Displays directions for current bias test (NMOS)
    """
    display.clear()
    display.text("Testing Curr Bias (nmos):", 0,15)
    display.text("-Connect ammeter to I_REFN",0,45)
    display.text("-Confirm ~10 micro Amps;", 0,75)
    
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
                display.text("Passed NMOS Curr Bias Test",0, 15)
                display.text("Launching PMOS Curr Bias Test", 0,45)
                sleepMenu()
                runPmosCurrBiasTest(display,hardware)
                return
            else: #:NO
                display.clear()
                display.text("Test failed:Check connections", 0,15)
                display.text("Returning to menu...", 0,45)
                sleepMenu()
                return
        sleep_ms(50)

def pmosCurrBiasDirections(display):
    """
        Displays directions for current bias test (PMOS)
    """
    display.clear()
    display.text("Testing Curr Bias (pmos):", 0,15)
    display.text("-Connect ammeter to I_REFP",0,45)
    display.text("-Confirm ~10 micro Amps;", 0,75)

    
def runPmosCurrBiasTest(display,hardware):
    """
        Current Bias test for PMOS
        If passed, returns to menu 
    """
    highlight = 0
    pmosCurrBiasDirections(display)
    yesNoMenu(highlight,display)
    while True:
        step = hardware.scrolling()    # –1, 0, or +1
        if step != 0:
            highlight = (highlight + step) % len(options)
            pmosCurrBiasDirections(display)
            yesNoMenu(highlight,display)
            sleep_ms(200)

        if hardware.isPressed():
            if options[highlight] == "YES":
                display.clear()
                display.text("Passed PMOS Curr Bias Test",0, 15)
                display.text("Place jumper on IREF_N/P", 0, 45)
                display.text("Returning to Menu...", 0,75)
                sleepMenu()
                return
            else: #:NO
                display.clear()
                display.text("Test failed:Check connections", 0,15)
                display.text("Returning to menu...", 0,45)
                sleepMenu()
                return
        
def RODirections(display):
    """
        Displays directions for Ring Oscillator test
    """
    display.clear()
    display.text("Testing 3 Ring Oscillator:", 0,15)
    display.text("-Programming Chip",0,45)
    display.text("-Place scope at STAGE1,2,3",0,75)
    display.text("-Confirm for correct waveforms", 0,105)
    
def runROTest(display,hardware):
    """
        Programs the chip for a 16-16-8 ring oscillator
        Prompts user to check for correct waveform on oscilloscope to pass
        Asks to check waveform for stage 1,2,3
    """ 
    highlight = 0
    RODirections(display)
    en.value(0)
    sleep(2)
    program()
    yesNoMenu(highlight,display)
    while True:
        step = hardware.scrolling()    # –1, 0, or +1
        if step != 0:
            highlight = (highlight + step) % len(options)
            RODirections(display)
            yesNoMenu(highlight,display)
            sleep_ms(10)

        if hardware.isPressed():
            if options[highlight] == "YES":
                display.clear()
                display.text("Passed 3 Ring Oscillator Test",0, 15)
                display.text("Returning to Menu...", 0,45)
                sleepMenu()
                en.value(0) 
                return
            else: #:NO
                display.clear()
                display.text("Test failed:Check connections", 0,15)
                display.text("Returning to menu...", 0,45)
                sleepMenu()
                en.value(0) 
                return
        sleep_ms(50)


