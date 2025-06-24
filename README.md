Current testing process: 
![testFlow]("C:\Users\Kayk7\Pictures\Screenshots\testingFlow.png")
**How to use:**
1. Using LCD:
Note: This uses the ILI9341 LCD
  - Download all files in the lcd_interface folder to the Raspberry Pi Pico
  - Download all files in the lcd_tests folder
  !! NAME ALL FILES AS THEY ARE NAMED IN THE FOLDERS WHEN DOWNLOADING TO RASPBERRY PI PICO !!
  - Run mainLCD.py to start program

1.2 LCD Hardware (change as needed)
-Pins for Rotary Encoder)
  sw Pin(13) 
  dt Pin(14)
  clk Pin(15)
-Pins for LCD Display
  COPI (coordinator out participant in) Pin(19)
  CIPO (coordinator in participant out) Pin(16)
  cs Pin(26)
  dc Pin(28)
  sck Pin(18)
  rst Pin(6)
-Pins for tests
  ADC Pin(27)
  signal Pin(1)

2. Using OLED: 
Note: These files contain older versions of the interface 
  - Download all files in the oled_interface folder to the Raspberry Pi Pico
  - Download all files in the oled_tests folder
  !! NAME ALL FILES AS THEY ARE NAMED IN THE FOLDERS WHEN DOWNLOADING TO RASPBERRY PI PICO !!
  - Run main.py to start program

   
Used repositories: (Download and upload to the Raspberry Pi Pico) 
1. For LCD: rdagger micropython-ili9341: https://github.com/rdagger/micropython-ili9341
2. For OLED: rdagger/micropython-ssd1306: https://github.com/rdagger/micropython-ssd1306
