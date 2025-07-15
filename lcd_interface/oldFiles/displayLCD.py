from machine import Pin, SPI
from ili9341 import Display as IliDisplay, color565

class Display:
    def __init__(self, width=320, height=240, rotation=270, sck=18, mosi=19, miso=16, cs=26, dc=28, rst=27):
        try:
            spi = SPI(0, baudrate=32000000, sck=Pin(sck), mosi=Pin(mosi), miso=Pin(miso))
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

