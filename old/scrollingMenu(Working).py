from machine import Pin, I2C
from time import sleep 

#### Testing if button is being read ####
# while True: 
#     if test.value() == 1:
#         print("TURNED ON")
#         sleep(1) 
#         
#     elif test.value() == 0: 
#         print("TURNED OFF")
#         sleep(1) 

#### LEFT button for scrolling menu ####
#### RIGHT button for selection #### 
testButton = Pin(17, Pin.IN, Pin.PULL_DOWN)
selectionButton = Pin(16, Pin.IN, Pin.PULL_DOWN)
options = ['Test One', 'Test Two', 'Test Three', 'Test Four']
currOption = 0
i2cAddr = 0x72 #Display 
i2c = I2C(1, scl = Pin(27), sda = Pin(26), freq = 40000)

## Clear screen helper function ##
def resetScreen():
    i2c.writeto(i2cAddr, bytearray([0xFE, 0x01]))
    i2c.writeto(i2cAddr, bytearray([0xFE, 0x0D]))
    i2c.writeto(i2cAddr, bytearray([0xFE, 0x80 + 0])) 
    
resetScreen()
selected = options[currOption]
i2c.writeto(i2cAddr, selected.encode())
print(selected)
while True:
    if testButton.value() == 1:
        currOption = (currOption + 1) % len(options)
        sleep(0.1)
        selected = options[currOption]
        resetScreen()
        print(selected)
        i2c.writeto(i2cAddr, selected.encode()) 
        sleep(0.1)
    if selectionButton.value() == 1:
        print(f"Running: {selected}")
        resetScreen()
        i2c.writeto(i2cAddr, b'Running: \r')
        i2c.writeto(i2cAddr, selected.encode()) 
        sleep(0.1)
    sleep(0.1) 
    
