import pyautogui
from gestures import fingers, volume
import cv2 
import math
import numpy as np
level = 0
def cam():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    c = 0
    count = 0
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img , landmarks= fingers.detections(img)
        h, w = img.shape[0],img.shape[1]
        
        if c == 0:  #detecting gesture
            c = play_pause(landmarks, h, w)
            if c == 1:  #play and pause gesture detected
                pyautogui.press("space")
            elif c == 2:  #stop gesture detected
                pyautogui.press("w")
            elif c == 3:  #forward gesture detected
                pyautogui.press("d")
            elif c == 4:  #stop gesture detected
                pyautogui.press("a")
        if landmarks == []: #hand out of frame
            c = 0

        cv2.imshow("image",img)
        k = cv2.waitKey(1)
        if k == ord('q'):
            stop = True
            break

def position(landmarks, index, h, w):
    cx = int(landmarks[index].x * w)
    cy = int(landmarks[index].y * h)
    return cx, cy

def play_pause(landmarks, h, w): 
    if(len(landmarks) !=0):
        l8x, l8y = position(landmarks, 8, h, w)
        l5x, l5y = position(landmarks, 5, h, w)
        l12x, l12y = position(landmarks, 12, h, w)
        l9x, l9y = position(landmarks, 9, h, w)
        l16x, l16y = position(landmarks, 16, h, w)
        l13x, l13y = position(landmarks, 13, h, w)
        l20x, l20y = position(landmarks, 20, h, w)
        l17x, l17y = position(landmarks, 17, h, w)
        l4x, l4y = position(landmarks, 4, h, w)

        distance =  int(math.sqrt((l4x-l8x)**2 + (l4y - l8y)**2))
        print(distance)
        level = np.interp(distance, [20,100],[-65.25,0.0])
        volume.init(level)
        
        if l8y<l5y and l12y<l9y and l16y<l13y and l20y<l17y:    #pause_play
            return 1
        elif l8y>l5y and l12y>l9y and l16y>l13y and l20y>l17y:  #stop
            return 2
        elif l8y<l5y and l12y<l9y and l16y>l13y and l20y>l17y and l8x > l5x and l12x > l9x:  #forward
            return 3
        elif l8y<l5y and l12y>l9y and l16y>l13y and l20y>l17y and l8x < l5x and l12x < l9x:  #rewind
            return 4
        else:
            return 0
    else:
        return 0
