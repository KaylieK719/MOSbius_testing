#Menu.py V2
#- Changes to menu list logic (no longer based on files saved on RPI Pico)
#- Changes to drawMenu function/logic (combined all drawing menu functions into one) 
#- Updates to scrolling logic to accomodate menu & submenu 
#- Added main menu options & submenu options 
#- Removed scanFiles function 
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
#NOTE: To add tests, add the test name to self.PCBTests or self.chipTests and UPDATE the HELPERFUNCTIONS.PY 
#      module
        self.PCBTests = ["Power Test", "Digital Level Shifter Test", "Manual Enable Test",
                         "ALL TESTS", "BACK"]
        self.chipTests = ["Test One", "Test Two", "Test Three", "ALL TESTS", "BACK"]
        self.files = self.mainMenuTests
        self.currMenu = "MAIN"
        self.step = 0

    def drawMenu(self,files):
        display = self.display
        display.clear()
        fileSection = files[self.shift:self.shift + self.totalLines]

        for row, fileName in enumerate(fileSection, start=1):
            y = (row - 1) * self.lineHeight + 4
            if row + self.shift == self.highlight:
                # draw highlight bar
                display.fill_rect(0,y - 2,display.width,self.lineHeight,color565(255, 255, 255))

                display.text("> " + fileName, 4, y)
            else:
                display.text("  " + fileName, 4, y)

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
        
        #Deals with scrolling on the correct menu 
        if self.currMenu == "MAIN":
            self.drawMenu(self.files)
        elif self.currMenu == "PCB":
            self.drawMenu(self.files)
        else: #"CHIP"
            self.drawMenu(self.files)
        #Current file selected 
        print("Selected:", self.files[self.step])


