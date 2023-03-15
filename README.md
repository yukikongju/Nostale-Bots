# Nostale Bots

Disclaimer: This repository has been made for **learning purposes**. Please 
don't use these bots in the game.

## Requirements

```
pip install -r requirements.txt --user
python -m notebook
```

## Understanding How the Bots Work

We will use [yolov7](https://github.com/WongKinYiu/yolov7) for object detection.
To do so, we will need to create and annotate our dataset using either
[roboflow](https://app.roboflow.com/) or [labelImg](https://github.com/tzutalin/labelImg). 
This process can be quite tedious because we need to label over 150+ 
images. Once the bot can detect the object, we just need to tell the bot 
what command to execute. We will accomplish this task using [pyautogui](https://pypi.org/project/PyAutoGUI/).


## Meet the Bots


Mini-games bots:
- [ ] Woodcutting
- [ ] Rock Mining
- [ ] Fishing Pond
- [ ] Chicken Shooting

AoE/PvE bots:
- [ ] Pii Pod Bot: attack Pii Pod tree automatically


## Making the Bots

**Rock Mining**

The labeled dataset can be found [here](https://universe.roboflow.com/nostale-rock-mining/nostale-rock-mining)

**Pii Pod Bot**

## Clicking Mechanism

We want to simulate human clicking: when we cast a spell, we tend to 
click 2-3 times
