import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode = False,max_num_hands = 1,min_detection_confidence = 0.7)

def detections(img):
    #img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    master = []
    if results.multi_hand_landmarks:
        for hmark in results.multi_hand_landmarks:
                #for id, lm in enumerate(hmark.landmark):
                    #print(id, lm)
            master[:] = hmark.landmark[:]
            mp_drawing.draw_landmarks(img, hmark, mp_hands.HAND_CONNECTIONS)
    
    return img, master