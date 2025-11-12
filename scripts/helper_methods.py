import os
import pyautogui
import time
import numpy as np
import cv2
from PIL import Image
import random
from matplotlib.pyplot import imshow
from secrets1.secret import password, email
from matplotlib import pyplot as plt


clint_pos = [-1, -1] # (50, 31)
def_clint = [100, 100]


# up to am max of 10
def compare_img_screenshot(im,pos):
    width, height = im.size
    im2 = pyautogui.screenshot(region=(pos[0], pos[1], width, height))
    # im2.show()
    for i in range(0, min(width, max(25, width))):
        for j in range(0, min(height, max(25, height))):
            if (int(im.getpixel((i,j))[0] - im2.getpixel((i,j))[0])!=0):
                return False
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
def imagesearch(image, precision=0.7):
    im = pyautogui.screenshot(region=(0, 0, 1300, 750))
    secs = time.time()
    # im.save(f'testarea3{secs}.png') # useful for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(im)
    
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    template = cv2.imread(image, 0)
    plt.imshow(img_rgb, interpolation='nearest')
    plt.show()
    plt.imshow(template, interpolation='nearest')
    plt.show()
    print('---------------------------------------------- HERE WE GO ----------------------------')
    print('was here 3000 years ago')
    print(img_rgb.shape[::-1])
    print('-----------#####-----------------------------')
    print(img_rgb[0].shape)
    print('-----------#####-----------------------------')
    print(template.shape[::-1])
    print('-----------#####-----------------------------')
    print(template[0].shape)
    print('-----------#####-----------------------------')
    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc




def reset_client_window():
    global clint_pos
    if clint_pos != [-1, -1]:
        if clint_pos == def_clint:
            return
        time.sleep(.5)
        pyautogui.moveTo(clint_pos[0], clint_pos[1])
        time.sleep(.5)
        pyautogui.mouseDown()
        time.sleep(.5)
        pyautogui.dragTo(x=def_clint[0], y=def_clint[1], duration=2.0, button='left')
        time.sleep(.5)
        pyautogui.mouseUp()
        time.sleep(.5)
        # time.sleep(2)




def find_login_button_and_click():
    time.sleep(.5)
    img = Image.open('images/login_button.png')
    if compare_img_screenshot(img,(1196, 406)):
        pyautogui.click(1196 + random.randrange(1,20), 406 + random.randrange(1,20))
        print("Login button clicked.")  
        time.sleep(1.5)
        return True
    time.sleep(.5)
    login_button_pos = imagesearch('images/login_button.png', precision=0.95)
    print("Login button position: ", login_button_pos)
    if login_button_pos != [-1, -1]:
        pyautogui.click(login_button_pos[0] + random.randrange(1,20), login_button_pos[1] + random.randrange(1,20))
        print("Login button clicked.")  
        time.sleep(1.5)
        return True
    return False



def login():
    time.sleep(2)
    if imagesearch('images/cashier.png', precision=0.95) != [-1, -1]:
        print("already logged in")
        return True
    find_login_button_and_click()
    #putting in credentials
    upper_corner = Image.open('images/login_popup_upper_corner.png')
    if compare_img_screenshot(upper_corner,(508, 191)):
        upper_corner_pos = (508, 191)
    else: 
        upper_corner_pos = imagesearch('images/login_popup_upper_corner.png', precision=0.95)    
        print("upper_corner position: ", upper_corner_pos)

    if upper_corner_pos != [-1, -1]:
        pyautogui.doubleClick(upper_corner_pos[0] + 236 , upper_corner_pos[1] + 120)
        time.sleep(.5)
        mails = email.split('-at-')
        pyautogui.typewrite(mails[0], interval=0.2)
        pyautogui.hotkey('altright','q') # typing @
        pyautogui.typewrite(mails[1], interval=0.2)
        time.sleep(.5)
        pyautogui.doubleClick(upper_corner_pos[0] + 236, upper_corner_pos[1] + 160)
        time.sleep(.5)
        pyautogui.typewrite(password, interval=0.5)
        time.sleep(.5)
    else:
        return "try again"

    logging_in_button = Image.open('images/logging_in_button.png')
    if compare_img_screenshot(logging_in_button,(582, 501)):
        pyautogui.click(582 + random.randrange(1,100), 501 + random.randrange(1,20))
        time.sleep(1.5)
        return True
    time.sleep(.5)
    login_button_pos = imagesearch('images/logging_in_button.png', precision=0.95)    
    print("second login button position: ", login_button_pos)
    if login_button_pos != [-1, -1]:
        pyautogui.click(login_button_pos[0] + random.randrange(1,100), login_button_pos[1] + random.randrange(1,20))
        print("second login button clicked.")  
        time.sleep(1.5)
        return True
    return 'try again'





def check_if_client_running(waiting = True):
    print("Checking if GGPoker client is running... waiting = "+str(waiting))
    gg_icon = Image.open('images/GG_icon1.png')
    if compare_img_screenshot(gg_icon,(100, 100)):
        # best & normal case scenario, the client is already running and focused
        print("GGPoker client is running.")
        return True
    global clint_pos
    for _ in range(10 if waiting else 1):
        time.sleep(1.5)
        if compare_img_screenshot(gg_icon,(100, 100)):
            print("GGPoker client is running.")
            return True
        time.sleep(.5)
        clint_pos = imagesearch('images/GG_icon1.png', precision=0.75)
        print(clint_pos)
        if clint_pos != [-1, -1]:
            print('Client position found at: ', clint_pos)
            if clint_pos != (100, 100):
                print("resetting client position on desktop.")
                reset_client_window()
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
        find_login_button_and_click()
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





def compare_img(im,img2):
    size=img2.size
    for i in range(0, size[0]):
        for j in range(0, size[1]):
            if (int(im.getpixel((i,j)[0]) - img2.getpixel((i,j))[0])!=0):
                print("compare image unsuccessful")
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


def imagesearcharea(image, x1, y1, x2, y2, precision=0.95, im=None):
    if im is None:
        im = region_grabber(region=(x1, y1, x2, y2))
        # im.save('testarea2.png') # usefull for debugging purposes, this will save the captured region as "testarea.png"

    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc












def click_two_times_please(image_path):
    time.sleep(.5)
    button_pos = imagesearch(image_path, precision=0.95)
    print(f"{image_path} position: ", button_pos)
    print("sleeping some secs...")  
    time.sleep(random.randrange(2,3))
    if button_pos != [-1, -1]:
        pyautogui.click(button_pos[0] + random.randrange(1,10), button_pos[1] + random.randrange(1,10))
        time.sleep(.5)
        pyautogui.click(button_pos[0] + random.randrange(1,10), button_pos[1] + random.randrange(1,10))
        time.sleep(.5)
        print(f"{image_path} clicked 2x.")  
        return True
    return False


def click_one_times_please(image_path):
    for _ in range(2):
        button_pos = imagesearch(image_path, precision=0.9)
        print(f"{image_path} position: ", button_pos)
        if button_pos != [-1, -1]:
            pyautogui.click(button_pos[0] + random.randrange(1,10), button_pos[1] + random.randrange(1,10))
            time.sleep(.5)
            print(f"{image_path} clicked 1x.")  
            return True
    return False



def see_if_there_is_l_info():
    img = Image.open('images/i_understand.png')
    if compare_img_screenshot(img,(630, 569)):
        pyautogui.click(630 + random.randrange(1,20), 569 + random.randrange(1,20))
        print("I Understand.")  
        time.sleep(.5)
        print("I was here #1")
        # click_one_times_please('images/i_understand.png')
        return True
    time.sleep(.5)
    l_info_pos = imagesearch('images/l_info_headline.png', precision=0.85)
    if (l_info_pos == [-1, -1]):
        return False
    else:
        print("L info headline position: ", l_info_pos)
        for _ in range(2):
            time.sleep(.5)
            result = click_one_times_please('images/i_understand.png')
            print("I understand , I was here #2 , result: "+str(result))
            if result:
                return True
        return False



def push_holdem():
    img = Image.open('images/holdem.png')
    if compare_img_screenshot(img,(443, 202)):
        pyautogui.click(443 + random.randrange(3,10), 202 + random.randrange(3,10))
        print("Holdem clicked.")  
        time.sleep(.5)
        return True
    push_holdem_pos = imagesearch('images/holdem.png')
    print("Holdem position: ", push_holdem_pos)
    for _ in range(3):
        time.sleep(.5)
        see_if_there_is_l_info()
        if push_holdem_pos != [-1, -1]:
            pyautogui.click(push_holdem_pos[0] + random.randrange(3,10), push_holdem_pos[1] + random.randrange(3,10))
            print("Holdem clicked.")
            if imagesearcharea('images/holdem_clicked.png', 600, 300, 1300, 750, precision=0.75) != [-1, -1]:
                print("Holdem confirmed clicked.")
                return True
        
    return False


def scroll_to_bottom():
    # from holdem button 
    pyautogui.moveTo(610 + random.randrange(3,10), 550 + random.randrange(3,10))
    pyautogui.scroll(-10)
    time.sleep(.1)
    pyautogui.scroll(-10)
    time.sleep(.1)
    pyautogui.scroll(-10)
    time.sleep(.1)
    pyautogui.scroll(-10)
    time.sleep(.1)
    pyautogui.scroll(-10)
    time.sleep(.1)
    pyautogui.scroll(-10)
    time.sleep(.1)
    pyautogui.scroll(-10)
    time.sleep(.1)
    pyautogui.scroll(-10)
    time.sleep(.1)
    pyautogui.scroll(-10)



def click_ok():
    for _ in range(10):
        if click_one_times_please('images/ok.png'):
            return True
        time.sleep(3)
    return False


def fold():
    fold_pos = imagesearch('images/fold.png', precision=0.8)
    print("Fold button position: ", fold_pos)
    if fold_pos != [-1, -1]:
        pyautogui.click(fold_pos[0] + random.randrange(1,20), fold_pos[1] + random.randrange(1,20))
        print("Fold button clicked.")  
        time.sleep(.5)
        return True
    return False

def open_cards():
    open_pos = imagesearch('images/open.png', precision=0.8)
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



def init_gui():
    pass