from machine import Pin, I2C, SoftI2C
from os import listdir
from time import sleep_ms
import ssd1306
import sys

# Rotary encoder pins
sw = Pin(13, Pin.IN, Pin.PULL_UP)
dt = Pin(14, Pin.IN, Pin.PULL_UP)
clk = Pin(15, Pin.IN, Pin.PULL_UP)

# Display setup - with error handling
try:
    i2c = SoftI2C(scl=Pin(17), sda=Pin(16), freq=400000)
    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
    display_connected = True
except Exception as e:
    print("Display initialization failed:", e)
    display_connected = False

# Menu variables
position = 0
highlight = 1
shift = 0
total_lines = 4 
line_height = 15

def get_files():
    try:
        files = listdir()
        return [file for file in files if file.endswith(".py")]
    except Exception as e:
        print("Error reading files:", e)
        return ["No files found"]

def show_menu(menu):
    global position, highlight, shift
    
    if not display_connected:
        print("Menu:", menu[shift:shift+total_lines])
        return
    
    try:
        oled.fill(0)
        
        list_length = len(menu)
        short_list = menu[shift:shift+total_lines]
        
        for i, item in enumerate(short_list):
            y_pos = i * line_height + 4
            if highlight == i + 1:
                oled.fill_rect(0, y_pos - 2, oled_width, line_height, 1)
                oled.text("> " + item, 4, y_pos, 0)
            else:
                oled.text("  " + item, 4, y_pos, 1)
        
        oled.show()
    except Exception as e:
        print("Display error:", e)

def launch(filename):
    global file_list
    
    if not display_connected:
        print(f"Launching {filename}")
    else:
        try:
            oled.fill(0)
            oled.text("Launching", 30, 25)
            oled.text(filename, 15, 40)
            oled.show()
        except Exception as e:
            print("Display error:", e)
    
    sleep_ms(1000)
    
    try:
        with open(filename) as f:
            script = f.read()
        exec(script, globals())
    except Exception as e:
        print(f"Error executing {filename}:", e)
        if display_connected:
            try:
                oled.fill(0)
                oled.text("Error running:", 10, 20)
                oled.text(filename, 10, 35)
                oled.show()
                sleep_ms(2000)
            except:
                pass
    
    show_menu(file_list)

# Rotary encoder logic 
last_clk_val = clk.value()
file_list = get_files()

def scrolling():
    global position, highlight, shift, last_clk_val, file_list
    dt_val = dt.value()
    clk_val = clk.value()
    
    if last_clk_val == 1 and clk_val == 0: # falling edge
        if dt_val == 1:
            # Clockwise rotation
            if highlight < min(total_lines, len(file_list)):
                highlight += 1
            else:
                if shift + total_lines < len(file_list):
                    shift += 1
            position = (shift + highlight) - 1
        else:
            # Counter-clockwise rotation
            if highlight > 1:
                highlight -= 1
            else:
                if shift > 0:
                    shift -= 1
            position = (shift + highlight) - 1
        
        show_menu(file_list)
        print(f"Selected: {file_list[position]}")
    
    last_clk_val = clk_val

def is_pressed():
    global file_list, position
    if sw.value() == 0:
        sleep_ms(200)  # Debounce delay
        if len(file_list) > 0:
            print(f"Launching: {file_list[position]}")
            launch(file_list[position])
        else:
            print("No files available")

# Initial display
show_menu(file_list)

# Main loop
while True:
    try:
        scrolling()
        is_pressed()
        sleep_ms(10)
    except Exception as e:
        print("Main loop error:", e)
        sleep_ms(1000)
