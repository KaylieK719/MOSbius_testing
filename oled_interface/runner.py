from time import sleep_ms

def launch(display, filename):
    if display.connected:
        display.clear()
        display.text("Launching", 30,25)
        display.text(filename, 15,40)
        display.show()
    else:
        print("Launching", filename)
    sleep_ms(1000)

    try:
        code = open(filename).read()
        exec(code, globals())
    except Exception as e:
        print("Error running", filename, e)
    # redraw menu after script ends
