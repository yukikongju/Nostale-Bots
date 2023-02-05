# Nostale Bots

Disclaimer: This repository has been made for **learning purposes**. Please 
don't use these bots in the game.

## Requirements

To run the bots, you will need to install python libraries and the yolov7 model.

**Installing the Python Libraries**

To install the python libraries, run the command `pip install -r requirements.txt --user`
in your terminal

**Installing yolov7**

The instruction can be found [here](https://github.com/WongKinYiu/yolov7)


## Understanding how the bots work

Making our bots work requires two steps:
1. Object Traking: our bots need to know where are the ennemis
2. Making decision: once our bots have knowledge about the environment, they 
   need to decide what action they have to take. 

To track the objects, we will use the following methods:
- Using `opencv` template matching: periodically, we will take a screenshot 
   of the screen and tell opencv to find the images of the object on the screen. 
   We will then track their movement across time to find object speed.
- Using `yolo-v7`: we first perform transfer learning on the yolo model. To do 
   so, we will need to create our dataset using `pyautogui` to take screenshot 
   of the gameplay. We will then anotate each picture and draw bounding boxes 
   around the object we want to track. This process can be quite tedious because 
   we need to label 500+ images and the images need to be diverses. 
   To see how we applied transfer learning on yolov7, see the notebook by 
   executing `python -m notebook`

To decide what action our bots need to make, we will use the following strategies:
- Hard-coded action: we will use object tracking to find ennemis speed by tracking 
  ennemis position across time, and using that information, we can predict 
  the position of the object. We will then track the screen region associated 
  with the action and the bot will move only when the ennemis is in that region. 
  This strategy will help us reduce computation time 
  since we will only call the object detection program every 0.5 seconds instead 
  of 0.05 seconds (10 times less)
- Using `reinforcement learning`: if the hard coded action don't work well enough, 
  we will implement a reinforcement learning model so that the bot can learn the 
  best policy to play the game. The caveat is that our bot will need about 3000+ 
  runs to be trained and each runs take about 2 minutes to complete. This make  
  training time around 100 hours to test out one set of hyperparameters, which 
  makes training unfeasible without parallelization and cloud computing
  

## The Tasks


**Minigame - Pond**




**Minigame - Rock**






**Minigame - Wood**




**Training - Pii Pod**



## Bot Performance

To be completed


## Testing if the bots can be detected

Developping the bots is only the first part of the problem. The second part 
is making sure that the bot isn't detected by the game engine, otherwise our 
account will get banned. Currently, the game industry are using the following 
strategies to detect cheating: 
- Monitoring computer ressources: cheating software tends to be ressources 
  intensive, so game developer can flag any account that use computer 
  resources above a set threshold. However, cheaters can now run these software 
  on another computer, making this cheating detection obsolete.
- Using community reporting: players are encouraged to report any players that 
  are suspect of cheating. However, this method produces a lot of false 
  positives because salty players tend to report their opponent when they 
  lose, which makes it harder for game masters to find the real culprit.
- Using behavioral analysis: cheaters tend to behave in a way that differs 
  from the normal behaviors


## The Datasets

**Mini-Games**

The labeled dataset can be found [here](https://universe.roboflow.com/nostale-rock-mining/nostale-rock-mining)

**Pii Pod Bot**


## Ressources

**Cheating Detection**

- [Detecting Cheaters in a Distributed Multiplayer Game - Justin Weisz](https://www.cs.cmu.edu/~jweisz/courses/docs/weisz03_DetectingCheaters.pdf)
- [Robust Vision-Based Cheat Detection in Competitive Gaming - Frosio](https://arxiv.org/pdf/2103.10031.pdf)
- [Probabilistic Approches to Cheating Detection in Online Games - Dmitri Botvich](https://www.researchgate.net/publication/221157498_Probabilistic_Approaches_to_Cheating_Detection_in_Online_Games)
- [A Novel Approach to the Detection of Cheating in Multiplayer Online Games](https://core.ac.uk/download/pdf/322332744.pdf)
- [Cheat Detection using ML within CS:GO](https://openworks.wooster.edu/cgi/viewcontent.cgi?article=11803&context=independentstudy)

