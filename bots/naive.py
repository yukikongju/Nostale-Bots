
""" 
Strategy: Hit space to find the closest ennemi and use skills to 
kill it. 
- Hit pick up once in a while (W)
- Hit space once in a while to find new ennemi
"""

import pyautogui
import pygetwindow
import math
import time
import random

def main():
    # get Nostale window
    window = pygetwindow.getWindowsWithTitle('Nostale')[0]
    window.activate()

    # initialize keys
    attacks_keys = ['space', '2', '3']
    attaks_keys_proba = {'space': 0.7, '2': 0.15, '3': 0.15}
    #  attacks_keys = ['1', '2', '3', '4', 'space']
    #  attacks_keys = ['space']
    pickup_key = 'w'
    sit_key = 'c'
    buffs_keys = ['r']
    #  keys = load_next_keys(attacks_keys)
    keys = load_next_keys_with_proba(attaks_keys_proba)
    start_time_pickup = time.time()
    start_time_buffs = time.time()
    start_time_move = time.time()
    start_time_sit = time.time()

    # running the bot
    while True: 
        if not keys:
            #  keys = load_next_keys(attacks_keys)
            keys = load_next_keys_with_proba(attaks_keys_proba)
        delay = compute_delay(epsilon=.100)

        # attack 
        key = keys.pop(0)
        print(key)
        time.sleep(delay)
        pyautogui.press(key)
        time.sleep(delay)
        pyautogui.press(key)
        time.sleep(delay)

        # check for pick up
        #  elapsed_time_pickup = time.time() - start_time_pickup
        #  if elapsed_time_pickup > 2:
        #      pyautogui.press(pickup_key)
        #      start_time_pickup = time.time()
        pyautogui.press(pickup_key)
        time.sleep(delay)

        # check for buffs
        elapsed_time_buffs  = time.time() - start_time_buffs
        if elapsed_time_buffs > 100:
            start_time_buffs = time.time()
            for buff_key in buffs_keys:
                pyautogui.press(buff_key)

        # moving the bot around FIXME
        elapsed_time_move = time.time() - start_time_move
        if elapsed_time_move > 3:
            start_time_move = time.time()
            x, y = get_random_screen_position(window)
            x_mid, y_mid = window.midleft
            pyautogui.click(x_mid + x, y_mid + y)

        # TODO: make character sit to recover
        elapsed_time_sit = time.time() - start_time_sit
        if elapsed_time_sit > 50:
            start_time_sit = time.time()
            pyautogui.press(sit_key)
            time.sleep(10)
        



def get_random_screen_position(window):
    """ 

    """
    x = math.floor(random.uniform(-550, 250))
    y = math.floor(random.uniform(-250, 250))
    return x, y



def compute_delay(epsilon):
    """ 
    Compute delay before clicking: human can hit 5 keys per second
    """
    return random.uniform(.200-epsilon, .200+2*epsilon)

def load_next_keys_with_proba(prob_dict, n=100):
    outcomes = list(prob_dict.keys())
    probabilities = list(prob_dict.values())
    keys = [random.choices(outcomes, weights=probabilities, k=1)[0] for _ in range(n)]
    return keys

def load_next_keys(possible_keys, n=100): # TODO: add proba
    """ 
    Generate list of next keys to hit: 
    """
    keys = [possible_keys[random.randint(0, len(possible_keys)-1)] for _ in range(n)]
    return keys

if __name__ == "__main__":
    main()
