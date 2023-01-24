import pyautogui 
import time
import keyboard
import os

from pathlib import Path

keyboard.wait('space')
image_counter = 0

PROJECT_DIR = Path(os.path.abspath(__file__)).parent
SUBDIR_NAME = 'Rock'
DOWNLOAD_PATH = f'{PROJECT_DIR}/images/{SUBDIR_NAME}'

if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)

# screenshot left half of the screen

while not keyboard.is_pressed('q'):
    #  screenshot = pyautogui.screenshot(region=(0, 0, 960, 1080)) # for left half screen
    #  screenshot = pyautogui.screenshot(region=(0, 0, 1250, 950)) # for 1024x700 config 
    screenshot = pyautogui.screenshot(region=(295, 215, 695, 550)) # for mini-game
    IMAGE_PATH = os.path.join(DOWNLOAD_PATH, f'img_{image_counter}.jpg')
    screenshot.save(IMAGE_PATH)
    time.sleep(0.2)
    image_counter += 1




