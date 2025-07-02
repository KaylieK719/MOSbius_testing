#Runner.py V2
#- Changes to launch function (New Parameters: testName & function) 
from time import sleep_ms
import helperFunctions

def launch(display, testName, function):
    if display.connected:
        display.clear()
        display.text("Launching " + testName, 160 - (len(testName)*8 + 80)//2 ,120)

    else: #No connection (failed to display LCD) 
        print("Launching", testName)
    sleep_ms(1000)
    
    function()



