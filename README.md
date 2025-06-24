# Current testing process: 
![testFlow](images/testingFlow.png)

# Uploading Files
## 1. Using LCD:
Note: This uses the ILI9341 LCD
  - Download all files in the lcd_interface folder to the Raspberry Pi Pico ( `mainLCD.py` `displayLCD.py` `hardwareLCD.py` `menuLCD.py` `runnerLCD.py` )
  - Download all files in the lcd_tests folder (e.g `powerTestV2.py` `digitalLvlTestV2.py` `manualENTestV2.py`)
    *Do NOT change the file names when downloading to the Raspberry Pi Pico*

### 1.2 LCD Hardware (change as needed)
    -Pins for Rotary Encoder:
      sw = Pin(13) 
      dt = Pin(14)
      clk = Pin(15)
    -Pins for LCD Display
      COPI (coordinator out participant in) = Pin(19)
      CIPO (coordinator in participant out) = Pin(16)
      cs = Pin(26)
      dc = Pin(28)
      sck = Pin(18)
      rst = Pin(6)
    -Pins for tests:
      ADC = Pin(27)
      signal = Pin(1)

## External Libraries *(Download and upload to the Raspberry Pi Pico)* 
### 1. LCD: rdagger micropython-ili9341:
    - https://github.com/rdagger/micropython-ili9341
### 2. OLED: rdagger/micropython-ssd1306: 
    - https://github.com/rdagger/micropython-ssd1306
