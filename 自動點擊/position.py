import pyautogui
import keyboard
import time

def check_pos():
    print(f"Left click to get position in screen")
    while True:
        if keyboard.is_pressed('q'):
            x, y = pyautogui.position()
            print(f"Mouse position: x={x}, y={y}")
            time.sleep(0.1)

if __name__ == '__main__':
    check_pos()