from machine import Pin,I2C
from time import sleep

#Setting up I2C and Opening Screen 
i2cAddr = 0x72
i2c = I2C(1, scl = Pin(27), sda = Pin(26), freq = 40000)


i2c.writeto(i2cAddr, bytearray([0xFE, 0x01]))
i2c.writeto(i2cAddr, bytearray([0xFE, 0x0D]))
i2c.writeto(i2cAddr, bytearray([0xFE, 0x80 + 0])) 	

i2c.writeto(i2cAddr, b"> 3-R.O  \r")
i2c.writeto(i2cAddr, b"> Other  \r")

#button checking + selecting the test
buttonRight = Pin(17, Pin.IN, Pin.PULL_DOWN)  # Internal pull-down resistor
buttonLeft = Pin(16, Pin.IN, Pin.PULL_DOWN)

lCount = 0
rCount = 0 

while True:
    buttonRightVal = buttonRight.value()
    buttonLeftVal = buttonLeft.value()

    
    if buttonRightVal == 1:
        rCount += 1
        if rCount == 2:
            rCount = 0 
            i2c.writeto(i2cAddr, bytearray([0xFE, 0x01]))
            i2c.writeto(i2cAddr, bytearray([0xFE, 0x80 + 0]))
            sleep(0.3)
            i2c.writeto(i2cAddr, b"> 3-R.O  \r")
            i2c.writeto(i2cAddr, b"> Other  \r")
        else:
            i2c.writeto(i2cAddr, bytearray([0xFE, 0x01]))
            i2c.writeto(i2cAddr, bytearray([0xFE, 0x80 + 0])) 
            sleep(0.3)
            i2c.writeto(i2cAddr, b"Testing 3RO \r")
            sleep(0.3)
        
    if buttonLeftVal == 1:
        lCount += 1
        if lCount == 2:
            lCount = 0
            i2c.writeto(i2cAddr, bytearray([0xFE, 0x01]))
            i2c.writeto(i2cAddr, bytearray([0xFE, 0x80 + 0]))
            sleep(0.3)
            i2c.writeto(i2cAddr, b"> 3-R.O  \r")
            i2c.writeto(i2cAddr, b"> Other  \r")
        else:         
            i2c.writeto(i2cAddr, bytearray([0xFE, 0x01]))
            i2c.writeto(i2cAddr, bytearray([0xFE, 0x80 + 0])) 
            sleep(0.3)
            i2c.writeto(i2cAddr, b"Testing Other \r")
            sleep(0.3)

#Steps After:
#     -Set up helper functions for clearing the screen and resetting the cursor
