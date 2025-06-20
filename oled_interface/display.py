from machine import Pin, SoftI2C
import ssd1306

class Display:
    def __init__(self, width=128, height=64, scl=17, sda=16):
        try: #try to connect the oled with i2c protocol 
            i2c = SoftI2C(scl=Pin(scl), sda=Pin(sda), freq=400000)
            self.oled = ssd1306.SSD1306_I2C(width, height, i2c)
            self.connected = True
        except Exception as e:
            print("OLED init failed:", e)
            self.connected = False

        self.width  = width
        self.height = height

    def clear(self):
        if self.connected:
            self.oled.fill(0)

    def text(self, text, x, y, invert=False):
        if not self.connected:
            print(f"OLED: {text}")
            return
        elif invert == True:
            color = 0
        else:
            color = 1
        self.oled.text(s, x, y, color)

    def fill_rect(self, x, y, width, height, color):
        if self.connected:
            self.oled.fill_rect(x, y, width, height, color)

    def show(self):
        if self.connected:
            self.oled.show()
 