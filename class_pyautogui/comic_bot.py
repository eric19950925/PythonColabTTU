import pyautogui
import time

def click():
    time.sleep(1)
    pyautogui.click()

def scroll():
    time.sleep(1)
    pyautogui.scroll(-250)

def read_one_page():
    for i in range(6):
        scroll()

    time.sleep(1)
    # 查看是否找到
    # npl = pyautogui.locateOnScreen("next_page.png",confidence=0.95)
    # print(npl)
    # 花費2秒移動游標，接著再點擊
    pyautogui.click((pyautogui.locateCenterOnScreen("next_page.png",confidence=0.95)), duration=2)

def main():
    # 將目標元件截圖，之後都讓pyautogui幫我們尋找他
    # pyautogui.screenshot('next_page.png', region=(0, 1045, 80, 35))
    for i in range(50):
        time.sleep(3)
        read_one_page()

main()
