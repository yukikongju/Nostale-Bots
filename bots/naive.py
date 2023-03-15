
""" 
Strategy: Hit space to find the closest ennemi and use skills to 
kill it. 
- Hit pick up once in a while (W)
- Hit space once in a while to find new ennemi
"""

import pyautogui
import time
import random

def main():
    attacks_keys = ['1', '2', '3', '4', 'space']
    pickup_key = 'w'
    buffs_keys = ['r']
    keys = load_next_keys(attacks_keys)
    start_time_pickup = time.time()
    start_time_buffs = time.time()
    #  print(keys)
    while True: 
        if not keys:
            keys = load_next_keys(attacks_keys)
        key = keys.pop(0)
        delay = compute_delay(epsilon=.100)
        time.sleep(delay)
        pyautogui.press(key)

        # check for pick up and buffs
        elapsed_time_pickup = time.time() - start_time_pickup
        if elapsed_time_pickup > 20:
            pyautogui.press(pickup_key)
            elapsed_time_pickup = 0

        # check for buffs
        elapsed_time_buffs  = time.time() - start_time_buffs
        if elapsed_time_buffs > 100:
            elapsed_time_buffs = 0
            for buff_key in buffs_keys:
                pyautogui.press(buff_key)

def compute_delay(epsilon):
    """ 
    Compute delay before clicking: human can hit 5 keys per second
    """
    return random.uniform(.200-epsilon, .200+2*epsilon)

def load_next_keys(possible_keys, n=100):
    """ 
    Generate list of next keys to hit
    """
    keys = [possible_keys[random.randint(0, len(possible_keys)-1)] for _ in range(n)]
    return keys

if __name__ == "__main__":
    main()
