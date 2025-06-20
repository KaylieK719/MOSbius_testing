import os
from displayLCD import Display
from ili9341 import color565

class Menu:
    def __init__(self, display, totalLines=8, lineHeight=15):
        self.display = display
        self.totalLines = totalLines
        self.lineHeight = lineHeight
        self.highlight = 1
        self.shift = 0
        self.files = self.scanFiles()
        self.step = 0

    def scanFiles(self):
        files = []
        try:
            for file in os.listdir():
                if file.endswith(".py"):
                    files.append(file)
        except:
            return ["No files found"]
        return files

    def draw(self):
        display = self.display
        display.clear()
        fileSection = self.files[self.shift:self.shift + self.totalLines]

        for row, fileName in enumerate(fileSection, start=1):
            y = (row - 1) * self.lineHeight + 4
            if row + self.shift == self.highlight:
                # draw highlight bar
                display.fill_rect(
                    0,
                    y - 2,
                    display.width,
                    self.lineHeight,
                    color565(255, 255, 255)
                )

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
        self.draw()
        print("Selected:", self.files[self.step])

