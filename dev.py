import pyautogui
import time
import numpy as np
import cv2
# from matplotlib import pyplot as plt

from scripts.shavkats_functions import imagesearch, reset_client_window, def_clint






def screenshot_area(point = (250, 250), size = [70, 30]):
    time.sleep(6.5)
    # reset_client_window(debug=False)
    im = pyautogui.screenshot(region=(point[0], point[1], size[0], size[1]))
    # secs = time.time()
    # im2 = pyautogui.screenshot(region=(8, 32, 50, 50))
    im.save('temp31.png')

screenshot_area(point=[400, 435])

 

