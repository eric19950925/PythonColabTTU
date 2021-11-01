import pyautogui
import time


def click():
    time.sleep(0.01)
    pyautogui.click()


def main():
    for i in range(100):
        click()

main()

# crazy way
# https://gist.github.com/DaWe35/0febd8b058e4476967d12675a622c989
