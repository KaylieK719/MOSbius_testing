## Combined Display,Hardware,Menu,Runner modules into one file 
## Changed from horizontal to vertical orientation
## Patched bugs with display
from machine import Pin, SPI
from ili9341 import Display as IliDisplay, color565
from time import sleep_ms
import helperFunctions

### DISPLAY MODULE 
class Display:
    def __init__(self, width=240, height=320, rotation=180, sck=14, mosi=15,miso = 8, cs=17, dc=19, rst=18):
        try:
            spi = SPI(1, baudrate=32000000, sck=Pin(sck), mosi=Pin(mosi), miso=Pin(miso))
            self.display = IliDisplay(spi, cs=Pin(cs), dc=Pin(dc), rst=Pin(rst),
                                      width=width, height=height, rotation=rotation)
            self.connected = True
        except Exception as e:
            print("ILI9341 init failed:", e)
            self.connected = False

        self.width = width
        self.height = height

    def clear(self):
        if self.connected:
            self.display.clear()

    def text(self, text, x, y, invert=False):
        if not self.connected:
            print(f"OLED: {text}")
            return
        if invert:
            color = color565(0,0,0)
        else:
            color = color565(255,255,255)
        self.display.draw_text8x8(x, y, text, color)

    def fill_rect(self, x, y, width, height, color):
        if self.connected:
            self.display.fill_rectangle(x, y, width, height, color)
            
#### HARDWARE MODULE
class Hardware:
    def __init__(self, sw = 13, dt = 20, clk = 21):
        self.sw  = Pin(sw, Pin.IN, Pin.PULL_UP)
        self.dt  = Pin(dt, Pin.IN, Pin.PULL_UP)
        self.clk = Pin(clk, Pin.IN, Pin.PULL_UP)

        self.lastClk = self.clk.value()

    def scrolling(self):
        """+1 CW, -1 CCW, 0 no movement."""
        dtVal  = self.dt.value()
        clkVal = self.clk.value()
        step = 0
        if self.lastClk == 1 and clkVal == 0:
            step =  1 if dtVal == 1 else -1
        self.lastClk = clkVal
        return step

    def isPressed(self):
        if self.sw.value() == 0:
            sleep_ms(200)
            return True
        return False

### MENU MODULE
class Menu:
    def __init__(self, display, totalLines=16, lineHeight=15):
        self.display = display
        self.totalLines = totalLines
        self.lineHeight = lineHeight
        self.highlight = 1
        self.shift = 0
        self.mainMenuTests = ["Test PCB", "Test Chip"]
        self.PCBTests = ["Power Test", "Digital Level Shifter Test", "DT digitalLvl Test",
                         "CK digitalLvl Test", "EN digitalLvl Test","Manual Enable Test",
                         "Test PCB", "BACK"]
        self.chipTests = ["Current Bias Test", "3-Ring Oscillator", "Test Three", "ALL TESTS", "BACK"]
        self.files = self.mainMenuTests
        self.currMenu = "MAIN"
        self.step = 0
        
    def drawMenu(self,files):
        display = self.display
        display.clear()
        fileSection = self.files[self.shift:self.shift + self.totalLines]

        for row, fileName in enumerate(fileSection, start=1):
            y = (row - 1) * self.lineHeight + 4
            if row + self.shift == self.highlight:
                # draw highlight bar
                display.fill_rect(0,y - 2,display.width,self.lineHeight,color565(255, 255, 255))

                display.text("> " + fileName, 4, y)
            else:
                display.text("  " + fileName, 4, y)
    
    def resetCursor(self):
        self.highlight = 1
        self.shift = 0
        self.step = 0 

    def moveCursor(self, step):
        if step == 1:  # Down
            if self.highlight < min(self.totalLines, len(self.files)):
                self.highlight += 1
            elif self.shift + self.totalLines < len(self.files):
                self.shift += 1
        elif step == -1:  # Up
            if self.highlight > 1:
                self.highlight -= 1
            elif self.shift > 0:
                self.shift -= 1
        self.step = self.shift + self.highlight - 1
        print(self.step)
        self.drawMenu(self.files)

#### RUNNER MODULE
def launch(display, hardware, testName, function):
    if display.connected:
        display.clear()
        display.text("Launching " + testName, 120 - (len(testName)*8 + 80)//2 ,120)

    else: #No connection (failed to display LCD) 
        print("Launching", testName)
    sleep_ms(1000)
    
    function(display,hardware)







