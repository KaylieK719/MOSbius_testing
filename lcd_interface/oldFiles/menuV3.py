# MenuV3.py
# Fixed bug with cursor indexxing to allow smooth toggling between TEST PCB, TEST CHIP, and Main Menu 

import os
from displayLCD import Display
from ili9341 import color565

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


