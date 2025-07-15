# Jianxun's MOSbius_MicroPython_Flow, adjusted to run with the tester interface 
# https://github.com/Jianxun/MOSbius_MicroPython_Flow 
import json
import sys
import MOSbius
from time import sleep_ms 

PIN_EN = 10
PIN_CLK = 11
PIN_DATA = 12

def program():

    if sys.implementation.name == 'micropython':
        from machine import Pin
        pin_en = Pin(PIN_EN,Pin.OUT)
        pin_clk = Pin(PIN_CLK,Pin.OUT)
        pin_data = Pin(PIN_DATA,Pin.OUT)

        chip = MOSbius.mosbius_mk1(pin_en, pin_clk, pin_data)  
    else:
        # Not running on MCU, program_bitstream will not work.
        chip = MOSbius.mosbius_mk1()

    # Select connections file
    filename_connections = 'threeROConnections.json'
    
    with open(filename_connections,'r') as file:
        dict_connections = json.load(file)
        
    chip.create_bitstream(dict_connections)
    #chip.export_bitstream_to_csv()
    
    #optional debugging information
    chip.print_connections()
    chip.display_connections()
    
    chip.program_bitstream()

# if __name__ == "__main__":
#     main()
program()
