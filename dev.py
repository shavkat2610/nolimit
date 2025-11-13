import pyautogui
import time
import numpy as np
import cv2
from matplotlib import pyplot as plt

from scripts.helper_methods import imagesearch


def_clint = (70, 70)






def reset_client_window():
    clint_pos = imagesearch('images/GG_icon3.png', precision=0.75)
    if clint_pos != [-1, -1]:
        if clint_pos == def_clint:
            return
        time.sleep(.5)
        pyautogui.moveTo(clint_pos[0], clint_pos[1])
        time.sleep(.5)
        pyautogui.mouseDown()
        pyautogui.dragTo(x=def_clint[0]+300, y=def_clint[1]+200, duration=1.0, button='left')
        time.sleep(.5)
        pyautogui.dragTo(x=def_clint[0], y=def_clint[1], duration=1.0, button='left')
        clint_pos = def_clint
        time.sleep(.5)
        pyautogui.mouseUp()
        time.sleep(.5)
        # time.sleep(2)



def screenshot_area(point = (0, 0)):
    time.sleep(2.5)
    reset_client_window()
    im = pyautogui.screenshot(region=(point[0], point[1], 35, 20))
    # secs = time.time()
    # im2 = pyautogui.screenshot(region=(8, 32, 50, 50))
    im.save('temp.png')

screenshot_area(point=(418, 170))



