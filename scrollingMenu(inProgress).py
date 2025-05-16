### ADDING POTENTIOMETER AS SCROLLING MECHANISM ###

from machine import Pin,I2C,ADC
from time import sleep

#Setting up I2C and Opening Screen 
i2cAddr = 0x72
i2c = I2C(1, scl = Pin(27), sda = Pin(26), freq = 40000)


i2c.writeto(i2cAddr, bytearray([0xFE, 0x01]))
i2c.writeto(i2cAddr, bytearray([0xFE, 0x0D]))
i2c.writeto(i2cAddr, bytearray([0xFE, 0x80 + 0])) 	

## RIGHT Button is SELECT
## LEFT Button is SCROLL

buttonRight = Pin(17, Pin.IN, Pin.PULL_DOWN)  # Internal pull-down resistor
buttonLeft = Pin(16, Pin.IN, Pin.PULL_DOWN)

# options = [b"Test 1 \r", b"Test 2 \r", b"Test 3 \r", b"Test 4 \r"]
options = [1,2,3,4]
currOption = 0

if buttonLeft == 1:
    currOption += 1
    selected = options[currOption]
    print(selected) 
