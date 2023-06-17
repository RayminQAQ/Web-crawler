from pyautogui import moveTo, click
import keyboard
from time import sleep

def click(x,y):
    moveTo(x, y)
    click()

def event():
    while True:
        if keyboard.is_pressed('ESC'):
            break
        elif keyboard.is_pressed('space'):
            # Implementation
            click(100,100)
            sleep(0.1)


if __name__ == '__main__':
    event()