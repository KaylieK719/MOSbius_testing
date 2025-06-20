import hardwareLCD
from displayLCD import Display
from menuLCD import Menu
from runnerLCD  import launch
from time    import sleep_ms

def main():
    disp = Display()
    menu = Menu(disp)
    menu.draw()

    while True:
        step = hardwareLCD.scrolling()
        if step != 0:
            menu.moveCursor(step)

        if hardwareLCD.isPressed():
            launch(disp, menu.files[menu.step])
            menu.draw()

        sleep_ms(10)

if __name__ == "__main__":
    main()

