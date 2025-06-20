#importing modules and running loop
import hardware
from display import Display
from menu import Menu
from runner  import launch
from time    import sleep_ms

def main():
    disp = Display()
    menu = Menu(disp)
    menu.draw()

    while True:
        step = hardware.scrolling()
        if step != 0:
            menu.moveCursor(step)

        if hardware.isPressed():
            launch(disp, menu.files[menu.step])
            menu.draw()

        sleep_ms(10)

if __name__ == "__main__":
    main()
