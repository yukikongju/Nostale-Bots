import pyautogui 
import time
import keyboard
import os
import cv2

from pathlib import Path

keyboard.wait('space')
image_counter = 0

PROJECT_DIR = Path(os.path.abspath(__file__)).parent
SUBDIR_NAME = 'Wood'
DOWNLOAD_PATH = f'{PROJECT_DIR}/images/{SUBDIR_NAME}'

if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)

#  tmp = pyautogui.screenshot(region=(295, 215, 695, 550)) # mini-game window
#  upper_log = pyautogui.screenshot(region=(490, 500, 150, 100)) 
#  lower_log = pyautogui.screenshot(region=(490, 620, 150, 100))

#  upper_log = pyautogui.screenshot(region=(530, 515, 65, 20)) 
#  lower_log = pyautogui.screenshot(region=(530, 645, 65, 20))

#  UPPER_LOG_PATH = os.path.join(DOWNLOAD_PATH, f'upper_log.jpg')
#  upper_log.save(UPPER_LOG_PATH)
#  LOWER_LOG_PATH = os.path.join(DOWNLOAD_PATH, f'lower_log.jpg')
#  lower_log.save(LOWER_LOG_PATH)
#  TMP_PATH = os.path.join(DOWNLOAD_PATH, f'tmp.jpg')
#  tmp.save(TMP_PATH)

# check if log is in the middle of chopping board
while not keyboard.is_pressed('q'):
    # check upper log
    r, g, b = pyautogui.screenshot(region=(530, 515, 65, 20)).getpixel((32, 10))
    #  chop_upper = True if r == 87 and g == 60 and b == 17 else False
    chop_upper = True if r > 70 and r < 150 else False
    print(r,g, b)

    # check lower log
    r, g, b = pyautogui.screenshot(region=(530, 645, 65, 20)).getpixel((32, 10))
    #  chop_lower = True if r == 87 and g == 60 and b == 17 else False
    chop_lower = True if r > 70 and r < 150 else False

    print(chop_upper, chop_lower)
    
    if chop_upper: 
        pyautogui.press('left')
    if chop_lower: 
        pyautogui.press('right')

    time.sleep(0.05)



