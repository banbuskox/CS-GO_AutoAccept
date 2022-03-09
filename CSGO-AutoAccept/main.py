import time
import threading
import pyautogui


def Thread1():
    while True:
        try:
            acc = pyautogui.locateOnScreen("accept_image.png", confidence=0.7)
            acc_co = pyautogui.center(acc)
            x, y = acc_co.x, acc_co.y
            pyautogui.moveTo(x, y)
            pyautogui.click(x, y)
            print("Found button!")
        except:
            time.sleep(0.1)


def Thread2():
    while True:
        try:
            acc = pyautogui.locateOnScreen("accept_image2.png", confidence=0.7)
            acc_co = pyautogui.center(acc)
            x, y = acc_co.x, acc_co.y
            pyautogui.moveTo(x, y)
            pyautogui.click(x, y)
            print("Found button!")
        except:
            time.sleep(0.1)


t1 = threading.Thread(target=Thread1, args=[])
t2 = threading.Thread(target=Thread2, args=[])
t1.start()
t2.start()
print("Auto Accept enabled")
