from scripts.shavkats_functions import read_game_rules
import pyautogui
import pygetwindow



# requires 5k to be on screen in order to read rules properly

# read_game_rules(debug = True)

x2,y2 = pyautogui.size()
x2,y2=int(str(x2)),int(str(y2))
print(x2//2)
print(y2//2)


z1 = pygetwindow.getAllTitles()
