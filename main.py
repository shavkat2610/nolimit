import os
import pyautogui
import time
import numpy as np
import cv2
from scripts.helper_methods import click_ok, compare_img, fold, imagesearch, check_if_client_running, find_login_button_and_click, imagesearcharea, \
                                        login, make_screenshot_of_area, read_game_rules, screenshot_area, see_if_there_is_l_info, push_holdem, scroll_to_bottom, click_two_times_please, \
                                            click_one_times_please, start_client_and_login, open_cards, start
import random

big_blind = 500

def start():
    time.sleep(2)
    if not check_if_client_running(waiting=False):
        print("starting up client and logging in...")
        start_client_and_login()
    else:
        login()
    time.sleep(5)
    see_if_there_is_l_info(debug = False)
    if push_holdem():
        time.sleep(.5)
        see_if_there_is_l_info()
        scroll_to_bottom()

    def click_selection_or_exit():
        image_path = 'images/5k.png'
        if not click_two_times_please(image_path, debug = False):
            print("Could not find selection, exiting...")
            exit()
    click_selection_or_exit()
    if see_if_there_is_l_info():
        click_selection_or_exit()
    click_one_times_please('images/join_table.png', debug=False)
    # if see_if_there_is_l_info():
    #     click_selection_or_exit()
    #     click_one_times_please('images/join_table.png')
    #     see_if_there_is_l_info()
    time.sleep(1)
    click_one_times_please('images/join_again.png', debug=False)
    time.sleep(5)
    click_ok(debug = True)  

start()




# in game loop
while True:
    read_game_rules()
    screenshot_area(point = (50, 50), size = [150, 150], file_name="temp2.png")
    # area = imagesearcharea('images/D.png', 600, 300, 700, 450, precision=0.95) # read dealer position in area
    # print("D - area: "+str(area))
    # secs = time.time()
    # area = imagesearcharea('images/ingame_upleft.png', 0, 0, 1300, 750, precision=0.95)
    # print("upper left corner - area: "+str(area))
    # make_screenshot_of_area(0, 0, 1100, 900, file_name=f"screenshots/debug_{secs}.png")
#     # if open_cards():
#     #     time.sleep(2)
#     # fold()
#     # mouse.move(1400 + random.randrange(1,400) , 900 + random.randrange(1,100), absolute=True, duration=0.01)
    time.sleep(10)


