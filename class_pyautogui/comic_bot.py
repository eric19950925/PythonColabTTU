import webbrowser
import pyautogui
import time



def click():
    time.sleep(0.1)
    pyautogui.click()

def scroll():
    time.sleep(0.5)
    pyautogui.scroll(-250)

def read_one_page():
    for i in range(6):
        scroll()

    time.sleep(1)
    pyautogui.click((pyautogui.locateCenterOnScreen("next_page.png",confidence=0.95)))

    # pyautogui.screenshot('next_page.png', region=(1225, 870, 80, 35))
    # pyautogui.locateOnScreen('next_page.png')
    # npl = pyautogui.locateOnScreen("next_page.png",confidence=0.95)
    # print(npl)
    # npl = pyautogui.center(npl)
    # print(npl)
    # pyautogui.click(npl.x, npl.y, duration=2)

    # pyautogui.click(npl.x, npl.y-(17*page), duration=2)
    # pyautogui.click(x=1300, y=830, duration=2)


def main():
    webbrowser.open_new_tab('https://comicbus.com/html/103.html')
    time.sleep(3)

    pyautogui.moveTo((pyautogui.locateCenterOnScreen("reverse_order.png",confidence=0.95)), duration=1)
    npl = pyautogui.locateOnScreen("reverse_order.png",confidence=0.95)
    print(npl)
    # pyautogui.moveTo(npl.left, npl.left+80, duration=1)
    pyautogui.click(npl.left-70, npl.top+70, duration=1)
    time.sleep(3)
    for i in range(50):
        time.sleep(3)
        read_one_page()

main()
