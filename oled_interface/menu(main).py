import os
from display import Display

class Menu:
    def __init__(self, display, totalLines=4, lineHeight=15):
        self.display     = display #pass display object to menu constructor (figures out what lines, highlight.etc..)
        self.totalLines = totalLines
        self.line_height = line_height
        self.highlight   = 1
        self.shift       = 0
        self.files       = self.scanFiles()
        self.step    = 0

    def scanFiles(self):
        try:
            for file in os.listdir():
                if f.endswith(".py"):
                    return file 
        except:
            return ["No files found"]

    def draw(self):
        display = self.display
        display.clear()
        fileSection = self.files[self.shift:self.shift+self.totalLines]

        for row, fileName in enumerate(fileSection, start=1):
            y = (row-1)*self.lineHeight + 4 # +4 to make space for highlight rect 
            if row == self.highlight:
                #y-2 is to make the rectangle around* the text
                d.fill_rect(0, y-2, d.width, self.lineHeight, 1)
                d.text("> "+fileName, 4, y, invert=True)
            else:
                d.text("  "+fileName, 4, y)
                #"   " = indent 
        d.show()

    def moveCursor(self, step):
        # step = +1 or -1
        if step == 1:  # down
            if self.highlight < min(self.totalLines, len(self.files)):
                self.highlight += 1
            elif self.shift + self.totalLines < len(self.files): #off the screen (down)
                self.shift += 1
        elif step == -1:  # up
            if self.highlight > 1: 
                self.highlight -= 1
            elif self.shift > 0: #off screen (up) 
                self.shift -= 1

        self.step = self.shift + self.highlight - 1
        self.draw()
        print("Selected:", self.files[self.step])
