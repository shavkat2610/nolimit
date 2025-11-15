import pyautogui
import time
import numpy as np
import cv2
# from matplotlib import pyplot as plt

from scripts.helper_methods import imagesearch, reset_client_window






def screenshot_area(point = (0, 0)):
    time.sleep(6.5)
    reset_client_window(debug=False)
    im = pyautogui.screenshot(region=(point[0], point[1], 250, 100))
    # secs = time.time()
    # im2 = pyautogui.screenshot(region=(8, 32, 50, 50))
    im.save('dark_icon_3.png')

screenshot_area(point=(420, 145))



