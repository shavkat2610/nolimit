import os
import pyautogui
import time
import numpy as np
import cv2
from PIL import Image
import random
# from matplotlib.pyplot import imshow
# import matplotlib
# matplotlib.use('agg')
from secrets1.secret import password, email
from matplotlib import pyplot as plt
# import pyperclip
import glob
import pytesseract




pull_to = [5, 25]
def_clint = [7, 50] #69, 70


def remove_debug_imgs():
    removing_files = glob.glob('temp_*.png')
    # removing_files_0 = glob.glob('temp_*.png')
    for i in removing_files:
        os.remove(i)


# up to am max of 10
def compare_img_screenshot(im,pos, max_ = 50, debug = True, debug_2 = True):
    # saving both if unsuccessful
    width, height = im.size
    secs = time.time()
    im2 = pyautogui.screenshot(region=(pos[0], pos[1], width, height))
    # im2.show()
    for i in range(0, min(width, max(max_, width))):
        for j in range(0, min(height, max(max_, height))):
            if im.getpixel((i,j))[0] - im2.getpixel((i,j))[0]!=0:
                if debug_2:
                    print(str(im.getpixel((i,j))[0])+" and "+str(im2.getpixel((i,j))[0]) + " are not the same")
                    print(im.getpixel((i,j)))
                    print(im2.getpixel((i,j)))
                    print(i, j)
                    im.save(f'temp_{secs}_1.png')
                    im2.save(f'temp_{secs}_2.png')
                return False
    if debug:
        print('compare_img_screenshot successful')
    return True





'''
Searchs for an image on the screen

input :

image : path to the image file (see opencv imread for supported types)
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
im : a PIL image, usefull if you intend to search the same unchanging region for several elements

returns :
the top left corner coordinates of the element if found as an array [x,y] or [-1,-1] if not

'''
def imagesearch(image_path, precision=0.9, debug = False, calling_function = None):
    im = pyautogui.screenshot(region=(0, 0, 1400, 1000))
    secs = time.time()
    # im2.save('temp.png')
    # im.save(f'testarea7_{secs}.png') # useful for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(im)
    # img2_rgb = np.array(im2)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    template = cv2.imread(image_path, 1)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
    # if debug:
    #     img4_rgb = np.array(im)
    #     print("imagesearch - from : "+str(calling_function))
    #     print('screenshot')
    #     plt.imshow(img4_rgb, interpolation='nearest')
    #     plt.show()
    #     print('looking for: ')
    #     plt.imshow(template, interpolation='nearest')
    #     plt.show()
    try:
        coordinates = pyautogui.locate(template, img_rgb, confidence=0.999)
        if debug:
            print('pyautogui located '+image_path+' - proceeding anyways with cv.matchTemplate')
        else:
            return [coordinates[0].__int__(), coordinates[1].__int__()]
    except:
        print(f'{image_path} not found at first glance')
    # plt.imshow(img2_rgb, interpolation='nearest')
    # plt.show()
    # plt.imshow(template, interpolation='nearest')
    # plt.show()
    template_gray = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
    # img_rgb.shape[::-1]
    res = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        print('not found')
        return [-1, -1]
    if debug:
        im2 = pyautogui.screenshot(region=(max_loc[0], max_loc[1], template_gray.shape[1], template_gray.shape[0]))
        print()
        print('found at '+str(max_loc) +" - at confidence: "+str(max_val))
        # if max_val > 0.999:
        #     return [max_loc[0], max_loc[1]]
        print(f'saving this ({image_path}) to memory: ')
        img2_rgb = np.array(im2)
        plt.imshow(img2_rgb, interpolation='nearest')
        plt.show()
        print('instead of this: ')
        plt.imshow(template, interpolation='nearest')
        plt.show()
        time.sleep(2)
        im2.save(image_path[:-4]+"_new.png")
    return [max_loc[0], max_loc[1]]




def reset_client_window(debug = False):
    clint_pos = imagesearch('images/GG_icon3.png', precision=0.9, debug=debug, calling_function= 'reset_client_window')
    if clint_pos != [-1, -1]:
        while True:
            if clint_pos == def_clint:
                return True
            print("clint_pos = "+str(clint_pos))
            pyautogui.moveTo(clint_pos[0]+3, clint_pos[1]+3)
            pyautogui.mouseDown()
            pyautogui.dragTo(x=def_clint[0]+20, y=def_clint[1]+20, duration=.2, button='left')
            pyautogui.dragTo(x=pull_to[0], y=pull_to[1], duration=.2, button='left')
            pyautogui.mouseUp()
            time.sleep(3) #temporary
            clint_pos = imagesearch('images/GG_icon3.png', precision=0.9, debug=debug, calling_function= 'reset_client_window')
            if clint_pos == def_clint:
                return True
            # time.sleep(2)
    else:
        print("reset window failed to locate GG_icon")
        sespos = imagesearch('images/session.png', precision=0.9, debug=debug, calling_function= 'reset_client_window')
        if sespos != [-1, -1]:
            print("sespos = "+str(sespos))
            pyautogui.moveTo(sespos[0]+3, sespos[1]+3)
            pyautogui.mouseDown()
            pyautogui.dragTo(x=1200, y=145, duration=0.5, button='left')
            pyautogui.mouseUp()
            time.sleep(.3)
            reset_client_window()
            # time.sleep(2)
        return False




def find_login_button_and_click():
    img = Image.open('images/login_button.png')
    if compare_img_screenshot(img,(1114, 352)):
        pyautogui.click(1115 + random.randrange(1,20), 352 + random.randrange(1,20))
        print("login clicked")
        time.sleep(.5)
        return True
    img2 = Image.open('images/login_button_2.png')
    if compare_img_screenshot(img2,(1114, 352)):
        pyautogui.click(1177 + random.randrange(1,20), 377 + random.randrange(1,20))
        print("login clicked (2)")
        time.sleep(.5)
        return True
    img0 = Image.open('images/login_button_0.png')
    if compare_img_screenshot(img0,(1114, 352)):
        pyautogui.click(1177 + random.randrange(1,20), 377 + random.randrange(1,20))
        print("login clicked (3)")
        time.sleep(.5)
        return True
    img3 = Image.open('images/login_button_3.png')
    if compare_img_screenshot(img3,(1114, 352)):
        pyautogui.click(1177 + random.randrange(1,20), 377 + random.randrange(1,20))
        print("login clicked (4)")
        time.sleep(.5)
        return True
    time.sleep(.5)
    login_button_pos = imagesearch('images/login_button.png', precision=0.9, calling_function= 'find_login_button_and_click')
    print("Login button position: ", login_button_pos)
    if login_button_pos != [-1, -1]:
        pyautogui.click(login_button_pos[0] + random.randrange(1,20), login_button_pos[1] + random.randrange(1,20))
        print("Login button clicked.")  
        time.sleep(.5)
        return True
    return False



def login(debug = False):
    img = Image.open('images/cashier_insted.png')
    if compare_img_screenshot(img,(1114, 352)):
        print("already logged in ")
        return True
    img_pos = imagesearch('images/cashier_insted.png', precision=0.9, debug=debug, calling_function= 'login')
    if img_pos != [-1, -1]:
        print("cashier position: ", img_pos)
        print("already logged in ")
        return True
    find_login_button_and_click()
    #putting in credentials
    upper_corner = Image.open('images/login_popup_upper_corner.png')
    if compare_img_screenshot(upper_corner,(420, 149)):
        upper_corner_pos = (420, 149)
    else: 
        upper_corner_pos = [-1, -1]
        while upper_corner_pos == [-1, -1]:
            upper_corner_pos = imagesearch('images/login_popup_upper_corner.png', precision=0.9, debug=debug, calling_function= 'login')
            print("upper_corner position: ", upper_corner_pos)

    if upper_corner_pos != [-1, -1]:
        pyautogui.doubleClick(upper_corner_pos[0] + 236 , upper_corner_pos[1] + 120)
        mails = email.split('-at-')
        pyautogui.typewrite(mails[0], interval=0.02)
        # pyautogui.hotkey('altright','q') # typing @
        if os.name == 'posix':  # macOS 
            pyautogui.hotkey('option', 'l')
        elif os.name == 'nt':  # Windows
            pyautogui.hotkey('altright','q') # typing @
        pyautogui.typewrite(mails[1], interval=0.02)
        pyautogui.doubleClick(upper_corner_pos[0] + 236, upper_corner_pos[1] + 160)
        pyautogui.typewrite(password, interval=0.02)
    else:
        return "try again"
    logging_in_button = Image.open('images/logging_in_button.png')
    if compare_img_screenshot(logging_in_button,(569, 455)):
        pyautogui.click(569 + random.randrange(1,100), 455 + random.randrange(1,10))
        return True
    login_button_pos = imagesearch('images/logging_in_button.png', precision=0.9, debug=debug, calling_function= 'login')
    print("second login button position: ", login_button_pos)
    if login_button_pos != [-1, -1]:
        pyautogui.click(login_button_pos[0] + random.randrange(1,100), login_button_pos[1] + random.randrange(1,10))
        print("second login button clicked.")
        return True
    return 'try again'





def check_if_client_running(waiting = True):
    print("Checking if GGPoker client is running... waiting = "+str(waiting))
    gg_icon = Image.open('images/GG_icon3.png')
    if compare_img_screenshot(gg_icon,(def_clint[0], def_clint[1]), debug=False):
        # best & normal case scenario, the client is already running and focused
        pyautogui.click(def_clint[0], def_clint[1])  
        print("GGPoker client is running.")
        return True
    global clint_pos
    for _ in range(7 if waiting else 1):
        if compare_img_screenshot(gg_icon,(def_clint[0], def_clint[1]), debug=False):
            print("GGPoker client is running.")
            return True
        time.sleep(.5)
        clint_pos = imagesearch('images/GG_icon3.png', precision=0.9, debug=False, calling_function= 'check_if_client_running')
        if clint_pos != [-1, -1]:
            print('Client position found at: ', clint_pos)
            if clint_pos != def_clint:
                print("resetting client position on desktop.")
                reset_client_window()
            else: pyautogui.click(clint_pos[0], clint_pos[1])
            return True   
    print("GGPoker client is not running.")
    return False




def start_client_and_login():
    print("Starting GGPoker client...")
    if os.name == 'posix':  # macOS 
        os.system("open /Applications/GGPoker.app")
    elif os.name == 'nt':  # Windows
        os.system("start C:/Users/shavk/AppData/Roaming/GGPCOM/bin/launcher.exe")

    time.sleep(15)

    if not check_if_client_running():
        print("Client is not running!")
        exit()

    while login() == "try again":
        print("try again")
        # find_login_button_and_click()
    return True







'''

grabs a region (topx, topy, bottomx, bottomy)
to the tuple (topx, topy, width, height)

input : a tuple containing the 4 coordinates of the region to capture

output : a PIL image of the area selected.

'''


def region_grabber(region):
    print("I was here at region graber #323")
    x1 = region[0]
    y1 = region[1]
    width = region[2] - x1
    height = region[3] - y1
    return pyautogui.screenshot(region=(x1, y1, width, height))





def compare_img(im,img2): # why is thos failing
    size=img2.size
    for i in range(0, size[0]):
        for j in range(0, size[1]):
            if abs(int(im.getpixel((i,j))[0] - img2.getpixel((i,j))[0]))>=5:
                im.getpixel((i,j))
                img2.getpixel((i,j))
                (i,j)
                print("compare image unsuccessful")
                input("Press Enter to continue...")
                return False
    print("compare image successful")
    return True











'''

Searchs for an image within an area

input :

image : path to the image file (see opencv imread for supported types)
x1 : top left x value
y1 : top left y value
x2 : bottom right x value
y2 : bottom right y value
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
im : a PIL image, usefull if you intend to search the same unchanging region for several elements

returns :
the top left corner coordinates of the element if found as an array [x,y] or [-1,-1] if not

'''


def imagesearcharea(image, x1, y1, width, height, precision=0.99, im=None):
    if im is None:
        im = pyautogui.screenshot(region=(x1, y1, width, height))
        # im = region_grabber(region=(x1, y1, x2, y2))
        # im.save('testarea2.png') # usefull for debugging purposes, this will save the captured region as "testarea.png"

    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc












def click_two_times_please(image_path, precision = 0.95, debug = False):
    time.sleep(.5)
    button_pos = imagesearch(image_path, precision=precision, debug = debug, calling_function="click_two_times_please")
    print(f"{image_path} position: ", button_pos)
    if button_pos != [-1, -1]:
        pyautogui.click(button_pos[0] + random.randrange(1,10), button_pos[1] + random.randrange(1,10))
        time.sleep(.5)
        pyautogui.click(button_pos[0] + random.randrange(1,10), button_pos[1] + random.randrange(1,10))
        time.sleep(.5)
        print(f"{image_path} clicked 2x.")  
        return True
    return False


def click_one_times_please(image_path, precision=0.9,  debug = False):
    for _ in range(3):
        button_pos = imagesearch(image_path, precision=precision, debug = debug, calling_function="click_one_times_please")
        # print(f"{image_path} position: ", button_pos)
        if button_pos != [-1, -1]:
            pyautogui.click(button_pos[0] + random.randrange(1,4), button_pos[1] + random.randrange(1,4))
            time.sleep(.5)
            print(f"{image_path} clicked 1x.")
            return True
    return False



def see_if_there_is_l_info(debug = False):
    time.sleep(.5)
    img = Image.open('images/i_understand.png')
    if compare_img_screenshot(img,(630, 569)):
        pyautogui.click(630 + random.randrange(1,20), 569 + random.randrange(1,20))
        print("I Understand.")  
        time.sleep(.5)
        # click_one_times_please('images/i_understand.png')
        return True
    time.sleep(.5)
    l_info_pos = imagesearch('images/l_info_headline.png', precision=0.75, debug = debug, calling_function="see_if_there_is_l_info")
    if (l_info_pos == [-1, -1]):
        return False
    else:
        print("L info headline position: ", l_info_pos)
        for _ in range(3):
            time.sleep(.5)
            result = click_one_times_please('images/i_understand.png', precision=0.75, debug = debug)
            print("I understand , I was here #2 , result: "+str(result))
            if result:
                return True
        return False


def push_holdem():
    img = Image.open('images/holdem_clicked.png')
    if compare_img_screenshot(img,(350, 142)):
        print("Holdem already clicked.")
        return True
    img = Image.open('images/holdem.png')
    if compare_img_screenshot(img,(350, 142)):
        pyautogui.click(350 + random.randrange(3,10), 142 + random.randrange(3,10))
        print("Holdem clicked.")  
        time.sleep(.5)
        return True
    push_holdem_pos = imagesearch('images/holdem.png', precision=.90, debug = False, calling_function="push_holdem")
    print("Holdem position: ", push_holdem_pos)
    for _ in range(3):
        time.sleep(.5)
        see_if_there_is_l_info()
        if push_holdem_pos != [-1, -1]:
            pyautogui.click(push_holdem_pos[0] + random.randrange(3,10), push_holdem_pos[1] + random.randrange(3,10))
            print("Holdem clicked.")
            time.sleep(.5)
            img = Image.open('images/holdem_clicked.png')
            if compare_img_screenshot(img,(350, 142)):
                print("Holdem confirmed clicked.")
                return True
            if imagesearch('images/holdem_clicked.png', precision=0.90, debug = False, calling_function="push_holdem") != [-1, -1]:
                print("Holdem confirmed clicked. 2")
                return True
        else:
            print("something went wrong somehow idk dude ...")
            if imagesearch('images/holdem_clicked.png', precision=0.90, debug = False, calling_function="push_holdem") != [-1, -1]:
                print("Holdem already clicked. 5")
                return True
            push_holdem_pos = imagesearch('images/holdem.png', precision=.90, debug = False, calling_function="push_holdem")
            see_if_there_is_l_info()
            if push_holdem_pos != [-1, -1]:
                pyautogui.click(push_holdem_pos[0] + random.randrange(3,10), push_holdem_pos[1] + random.randrange(3,10))
                print("Holdem clicked.")
                time.sleep(.5)
                img = Image.open('images/holdem_clicked.png')
                if compare_img_screenshot(img,(350, 142)):
                    print("Holdem confirmed clicked.")
                    return True
                if imagesearch('images/holdem_clicked.png', precision=0.90, debug = False, calling_function="push_holdem") != [-1, -1]:
                    print("Holdem confirmed clicked.")
                    return True
    return False


def scroll_to_bottom():
    # from holdem button 420, 555
    pyautogui.moveTo(420 + random.randrange(3,10), 555 + random.randrange(3,10))
    pyautogui.scroll(-5)
    time.sleep(.02)
    pyautogui.scroll(-5)
    time.sleep(.02)
    pyautogui.scroll(-5)
    time.sleep(.02)
    pyautogui.scroll(-5)
    time.sleep(.02)
    pyautogui.scroll(-5)
    time.sleep(.02)
    pyautogui.scroll(-5)
    time.sleep(.02)
    pyautogui.scroll(-5)
    time.sleep(.02)
    pyautogui.scroll(-5)
    time.sleep(.02)
    pyautogui.scroll(-5)
    time.sleep(.02)
    pyautogui.scroll(-5)
    time.sleep(.02)
    pyautogui.scroll(-5)
    time.sleep(.02)
    pyautogui.scroll(-5)
    time.sleep(.02)
    pyautogui.scroll(-5)



def click_ok(debug = False):
    image_path = 'images/ok.png'
    while True:
        button_pos = imagesearch(image_path, precision=0.95, debug = debug, calling_function="click_one_times_please")
        time.sleep(1.5)
        # print(f"{image_path} position: ", button_pos)
        if button_pos != [-1, -1]:
            pyautogui.click(button_pos[0] + random.randrange(10,14), button_pos[1] + random.randrange(1,4))
            print(f"{image_path} clicked 1x.")
            return True
    # return False






def fold():
    fold_pos = imagesearch('images/fold.png', precision=0.8, calling_function="fold")
    print("Fold button position: ", fold_pos)
    if fold_pos != [-1, -1]:
        pyautogui.click(fold_pos[0] + random.randrange(1,20), fold_pos[1] + random.randrange(1,20))
        print("Fold button clicked.")  
        time.sleep(.5)
        return True
    return False

def open_cards():
    open_pos = imagesearch('images/open.png', precision=0.8, calling_function="open_cards")
    print("Open button position: ", open_pos)   
    if open_pos != [-1, -1]:
        pyautogui.click(open_pos[0] + random.randrange(10,40), open_pos[1] + random.randrange(10,30))
        print("Open button clicked.")  
        time.sleep(.5)
        return True
    return False


def make_screenshot_of_area(x1, y1, x2, y2, file_name):
    im = region_grabber(region=(x1, y1, x2, y2))
    im.save(file_name)
    print(f"screenshot saved as {file_name}")

def screenshot_area(point = (50, 50), size = [250, 250], file_name = "temp.png"):
    time.sleep(3.5)
    im = pyautogui.screenshot(region=(point[0], point[1], size[0], size[1]))
    # secs = time.time()
    # im2 = pyautogui.screenshot(region=(8, 32, 50, 50))
    im.save(file_name)
    return im






import pygetwindow
dgrp = [468, 45]
def read_game_rules(big_blind = 200, debug = False):
    def click_selection_or_exit(big_blind=200):
        if big_blind == 200:
            image_path = 'images/5k.png'
            if not click_two_times_please(image_path, precision=90, debug = False):
                print("Could not find selection, exiting...")
                exit()
        else:
            pass #todo
    click_selection_or_exit(big_blind)
    if see_if_there_is_l_info():
        click_selection_or_exit(big_blind)
    
    click_one_times_please('images/join_table.png', debug=False) # debug false !
    time.sleep(3)

    click_one_times_please('images/join_again.png', debug=False) # debug false !
    time.sleep(5)

    click_ok(debug = False)  

    for _ in range(5):
        game_rules_pos = imagesearch('images/game_rules_color.png', precision=0.8, calling_function="read_game_rules", debug=debug)
        print("Game Rules position: ", game_rules_pos)
        if game_rules_pos != [-1, -1]:
            pyautogui.moveTo(game_rules_pos[0] - 300, game_rules_pos[1] + 3)
            pyautogui.mouseDown()
            pyautogui.dragTo(x=dgrp[0]+200, y=dgrp[1], duration=.7, button='left')
            time.sleep(.2)
            pyautogui.dragTo(x=dgrp[0], y=dgrp[1], duration=.7, button='left')
            pyautogui.mouseUp()
            # im = screenshot_area(point = (0, 100), size = [800, 530], file_name=f"game_screenshot.png")
            # # Setting the points for cropped image
            # left = 3
            # top = 20
            # right = 35
            # bottom = 400

            # # Cropped image of above dimension
            # # (It will not change original image)
            # im1 = im.crop((3, 20, 35, 400))

    return True





def run_it_up(big_blind = 200):
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

     # todo read_game_rules logic
     # # join table, 
     # # get game window, position top left corner
     # # check pixels, if it's in the exact right spot, read rules
     # # if not, move it to the right spot, then read rules
    read_game_rules(big_blind=big_blind, debug = False)


