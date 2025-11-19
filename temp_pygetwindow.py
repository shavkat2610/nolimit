# Source - https://stackoverflow.com/a/64489036
# Posted by tinus, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-17, License - CC BY-SA 4.0

import pygetwindow
import time
import os
import pyautogui
import PIL

# get screensize
x,y = pyautogui.size()
print(f"width={x}\theight={y}")

x2,y2 = pyautogui.size()
x2,y2=int(str(x2)),int(str(y2))
print(x2//2)
print(y2//2)

# find new window title
z1 = pygetwindow.getAllTitles()
print(z1)
time.sleep(1)
# test with GGPoker
if os.name == 'posix':  # macOS 
    os.system("open /Applications/GGPoker.app")
elif os.name == 'nt':  # Windows
    os.system("start C:/Users/shavk/AppData/Roaming/GGPCOM/bin/launcher.exe")
time.sleep(20)
z2 = pygetwindow.getAllTitles()
print(z2)
time.sleep(1)
z3 = [x for x in z2 if x not in z1]
z3 = z3[0]
print('z3: '+str(z3))
time.sleep(3)

# also able to edit z3 to specified window-title string like: "Sublime Text (UNREGISTERED)"
# my = pygetwindow.getWindowsWithTitle(z3)[0]
my = pygetwindow.getActiveWindow()
print(my)
exit()
# quarter of screen screensize
x3 = x2 // 2
y3 = y2 // 2
# my.resizeTo(x3,y3)
# top-left
my.moveTo(0, 0)
time.sleep(3)
my.activate()
time.sleep(1)

print("type(my): "+str(type(my)))

# save screenshot
p = pyautogui.screenshot()
p.save(r'./temp.png')

# edit screenshot
im = PIL.Image.open('./temp.png')
im_crop = im.crop((0, 0, x3, y3))
im_crop.save('./temp.jpg', quality=100)

# close window
time.sleep(1)
my.close()
