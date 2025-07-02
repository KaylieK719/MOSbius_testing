#Runner.py V2
#- Changes to launch function (New Parameters: testName & function) 
from time import sleep_ms
import helperFunctions

def launch(display, testName, function):
  """
    Takes 3 parameters: 
    1. display  
    2. testName (name of test to be run --> from self.PCBTests or self.chipTests)
    3. function (from helperFunctions module) 

    Checks if display is connected, displays launch text on LCD & runs function 
  """
    if display.connected:
        display.clear()
        display.text("Launching " + testName, 80,120)

    else: #No connection (failed to display LCD) 
        print("Launching", testName)
    sleep_ms(1000)
    
    function()


