from machine import Pin, I2C, SoftI2C
from time import sleep_ms
import ssd1306

sw = Pin(13, Pin.IN, Pin.PULL_UP)
dt = Pin(14, Pin.IN, Pin.PULL_UP)
clk = Pin(15, Pin.IN, Pin.PULL_UP)
i2c = machine.SoftI2C(scl= Pin(27), sda= Pin(26))

## Helper Functions ##
def pushDisplay():
    oled.show()

def initialize():
    oled.fill(0) 
    for y in range(len(tests)):
        oled.text(tests[y], 0, y*10)
        pushDisplay()
        
def testScreen(currPosition):
    oled.fill(0)
    oled.text('Testing', 30, 25)
    oled.text(f'{tests[currPosition % len(tests)]}...', 15,40)
    pushDisplay()

def rectSelection():
    selected = tests[position % len(tests)]
    initialize()
    oled.framebuf.rect(0, (position *10)%60, 128, 10, 1)
    pushDisplay()
    return

#Rotary logic 
lastClkVal = clk.value()
def scrolling():
    global position
    dtVal = dt.value()
    clkVal = clk.value()
    if lastClkVal == 1 and clkVal == 0: #falling edge
        if dtVal == 1:
            print("Clockwise")
            position += 1
            rectSelection()
            print(selected)
        else: #dtVal == 0
            print("Counter-Clock") 
            position -= 1
            rectSelection()
            print(selected)
    return

def isPressed():
    if sw.value() == 0:
        print(f"Testing {tests[position % len(tests)]}")
        testScreen(position)
    return 
        
## Rotary encoder 
position = 0
tests = ["3-Stage R.O", "Test 2", "Test 3", "Test 4",
         "Test 5", "Test 6"]
selected = tests[0]

## Initialization Display 
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
initialize()

## Checks for scrolling/button pressing
while True:
    scrolling()
    isPressed()
    sleep_ms(10)
    




    
