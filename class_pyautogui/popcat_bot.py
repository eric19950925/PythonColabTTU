import pyautogui
import time


def click():
    time.sleep(0.01)
    pyautogui.click()


def main():
    for i in range(100):
        click()

main()
