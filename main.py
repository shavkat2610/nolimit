import os
import pyautogui
import time
import numpy as np
import cv2
from scripts.shavkats_functions import click_ok, compare_img, fold, imagesearch, check_if_client_running, find_login_button_and_click, imagesearcharea, \
                                        login, make_screenshot_of_area, read_game_rules, run_it_up, screenshot_area, see_if_there_is_l_info, push_holdem, scroll_to_bottom, click_two_times_please, \
                                            click_one_times_please, start_client_and_login, open_cards, remove_debug_imgs
import random
import glob

big_blind = 200


remove_debug_imgs()


run_it_up(big_blind = big_blind)







def read_times(areas, areas_count):

    start = time.time()
    print("hello")
    end = time.time()
    print('{:f}'.format(end - start))

    secs = time.time()

    #in-game screenshot
    start = time.time()
    im = screenshot_area(point = (0, 100), size = [800, 530], file_name=f"temp_screenshot_{str(secs).split(".")[0]}.png")
    end = time.time()
    print('screenshot_area : {:f}'.format(end - start))

    start = time.time()
    area = imagesearcharea('images/D.png', 0, 100, 800, 530, precision=0.95, im = im) # read dealer position in area
    end = time.time()
    print('imagesearcharea : {:f}'.format(end - start))


    start = time.time()
    area = imagesearcharea('images/D.png', 0, 100, 800, 530, precision=0.95) # read dealer position in area
    end = time.time()
    print('imagesearcharea without image made before : {:f}'.format(end - start))

    print("D - area: "+str(area))
    if area not in areas:
        areas_count += 1
        print("new D-area: "+str(area))
        print("areas_count = "+str(areas_count))
        areas.append(area)

    start = time.time()
    pix = pyautogui.pixel(area[0]+4, area[1]+4+100)
    end = time.time()
    print('getting pixel from screen directly: {:f}'.format(end - start))

    print('pix: '+str(pix))

    start = time.time()
    pixels = im.load()
    end = time.time()
    print('pixels = im.load(): {:f}'.format(end - start))

    start = time.time()
    pixel_value = pixels[area[0]+4, area[1]+4]
    end = time.time()
    print('getting pixel from image: {:f}'.format(end - start))
    # print('pixels shape: '+str(pixels.))

    print("pixel_value : "+str(pixel_value))
    
    # pyautogui.pixelMatchesColor(area[0]+3, area[1]+3)
    # if open_cards():
    #     time.sleep(2)
    # fold()

    print('direct comparison: ')
    print(pixels[200, 200])
    print(pyautogui.pixel(200, 300))
    print('-----------------')
    print('another !')

    return areas, areas_count





def ingame_loop():
    areas_count = 0
    areas = []

    # mendatory
    while True:
        pyautogui.moveTo(1700, 950, duration=0.2)
        time.sleep(10)
        im = screenshot_area(point = (0, 100), size = [800, 530], file_name=f"temp_screenshot.png")
        pixels = im.load()
        pixel_value_0 = pixels[1, 14]
        pixel_value_1 = pixels[7, 18]
        pixel_value_2 = pixels[8, 25]
        print("pixel_value_0: "+str(pixel_value_0))
        print("pixel_value_1: "+str(pixel_value_1))
        print("pixel_value_2: "+str(pixel_value_2))
        # areas, areas_count = read_times(areas, areas_count)


ingame_loop()



