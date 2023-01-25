**Errors when downloading winpy**

1. Install `pywin32`
2. Make sure that there are no files starting with `~` in `lib/site-packages`
3. 

**Error CPU**

Yolov7 requires a GPU to be trained, so train the model on Google Colab to get a free GPU


## Todos

- [X] Download yolov5 or yolov7 
    - [X] Test it with dummy data
- [.] Gather Training Data with pyautogui 
    - [X] Pond
    - [ ] Rock Mining
    - [ ] Pii Pod
- [X] Label the data using ImgLabel
- [X] Train the model using transfer learning
    - [X] Configure `hyperparameters.yml` to not flip the images during training: change `fliplr` to 0.0
- [ ] Create yolov7 screen to view what the bot does
- [ ] Tell the bot what commands to do from object detection
- [ ] Play the game

## Making the Bot

**Rock Mining Mini-game**

Wiggler colors:
- [ ] Yellow
- [ ] Green
- [ ] Blue
- [ ] Red
- [ ] Purple

- Attempt 1: Using Yolov7: 
  + kind of a flop: yolov7 always guess yellow_right. Maybe I 
    should add more images in training data
  + [notebook](https://colab.research.google.com/drive/1nkpg66ECO5QN1le55V0VW0GjhbZT78yX#scrollTo=6AGhNOSSHY4_)
- Attempt 2: using opencv2 color detection: 
  1. Detect wiggler position and color using opencv
  2. find speed of wiggler 
  3. Calculate time before hitting bushtail
- Attempt 3: using reinforcement learning


## Ressources

- [Clarity Coders - AI Plays Toadled](https://www.youtube.com/watch?v=aNWvfF6TLlg)
- [Nicholas Renotte - Object Detection for Games](https://www.youtube.com/watch?v=0efnQCHbsyE)
- [Load YOLOv7 - Notebook](https://colab.research.google.com/drive/1nKoC-_areXmc_20Xn7z6kcqHEKU7SJsX#scrollTo=2S577j74Qcqa)
- [Loading Dataset](https://towardsdatascience.com/yolov7-a-deep-dive-into-the-current-state-of-the-art-for-object-detection-ce3ffedeeaeb)
- [Get Roboflow API - ](https://docs.roboflow.com/rest-api)
- [How to train and use custom YOLOv7 model](https://blog.paperspace.com/yolov7/)

