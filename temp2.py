
from PIL import Image
import pyautogui





ocsh1 = pyautogui.screenshot('sh.png',[444, 435, 333, 420])
ocsh1 = Image.open('sh.png')
ocsh1.save('sh.png')

