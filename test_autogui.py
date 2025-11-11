import pyautogui
import time
import numpy as np
import cv2

print(pyautogui.size())

card_pos = [[421,456,118,84],[148,396,118,84],[55,263,118,84],[94,135,118,84],[266,72,118,84],[576,72,118,84],[748,135,118,84],[787,263,118,84],[694,396,118,84]]
players_money = [[425,519,67,12],[152,459,67,12],[59,326,67,12],[98,198,67,12],[270,135,67,12],[623,135,67,12],[796,198,67,12],[835,326,67,12],[741,459,67,12]]
players_ID=[[480,500,40,12],[152,459,67,12],[59,326,67,12],[98,198,67,12],[270,135,67,12],[623,135,67,12],[796,198,67,12],[835,326,67,12],[741,459,67,12]]
"""
"""
#print(pyautogui.position())
position = pyautogui.position()
print(position)
# time.sleep(5)
print(pyautogui.pixel(position.x,position.y))

dealer_pos = [[394, 446],[247,361],[191,268],[296,213],[452, 168],[625,184],[737,236],[771,369],[651, 416]]
dealer_pix = [[218, 218, 218],[197,46,52],[200,72,79],[199,22,28],[179,41,46],[193, 193, 193],[194, 22, 27],[191, 191, 191],[246, 34, 43]]



confirm = 'OK'
seconds = time.time()
while (confirm == 'OK'):
    pyautogui.screenshot("C:/Users/shavk/Desktop/no_limit/ID_temp.png",
                         region=(players_ID[0][0], players_ID[0][1], players_ID[0][2], players_ID[0][3]))
    confirm = pyautogui.confirm('hi')
    if(confirm!='OK'):
        break
    new_seconds = time.time()
    print("seconds: "+str(new_seconds-seconds))
    seconds = time.time()
    # pyautogui.screenshot("D:/PyCharm/vitadrom/resources/temp/cards1.png",
    #                      region=(card_pos[8][0], card_pos[8][1], card_pos[8][2], card_pos[8][3]))
