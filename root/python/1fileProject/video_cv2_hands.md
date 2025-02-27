
![python_pCnSCvWFHR](https://github.com/user-attachments/assets/b21f62c9-b73d-442f-bdea-60a3993c6341)


![python_cYc9fJGeTX](https://github.com/user-attachments/assets/444da2d4-205e-4cd6-8445-1f243d9b057b)

![python_9fGkXUmJGV](https://github.com/user-attachments/assets/5cc0fa14-1266-4508-98a8-5b7c2b208814)

![python_A2LWZWUSgv](https://github.com/user-attachments/assets/a1c6783e-9afd-4a70-8a6b-2c962804a360)


``` bash
pip install pillow opencv-python mediapipe
```

``` py
import cv2
import mediapipe as mp
from PIL import Image
from math import sqrt
import numpy as np


def WRIST() -> None:
    """
    Prints a hand diagram with labeled landmarks, including wrist, thumb, and finger joints.
    Provides mapping of joint indices to their corresponding human-readable labels.
    """
    print('''
                     8        12         16          20
                    /        /          /           /
                   7        11        15           19
                  /        /         /           /
                 6        10        14         18
        4       /        /         /          /
         \     5--------9---------13--------17
          3     \                          /
           \       \                   /
            2         \            /
             \           \  0   /
              1-------------o

       WRIST:               0          ЗАП'ЯСТЯ
       THUMB_CMC:           1          ОСНОВА ВЕЛИКОГО ПАЛЬЦЯ
       THUMB_MCP:           2          П'ЯСТНО-ФАЛАНГОВИЙ СУГЛОБ
       THUMB_IP:            3          МІЖФАЛАНГОВИЙ СУГЛОБ
       THUMB_TIP:           4          КІНЧИК ВЕЛИКОГО ПАЛЬЦЯ
       INDEX_FINGER_MCP:    5          П'ЯСТНО-ФАЛАНГОВИЙ СУГЛОБ ВКАЗІВНОГО
       INDEX_FINGER_PIP:    6          ПРОКСИМАЛЬНИЙ СУГЛОБ ВКАЗІВНОГО
       INDEX_FINGER_DIP:    7          ДИСТАЛЬНИЙ СУГЛОБ ВКАЗІВНОГО
       INDEX_FINGER_TIP:    8          КІНЧИК ВКАЗІВНОГО ПАЛЬЦЯ
       MIDDLE_FINGER_MCP:   9          П'ЯСТНО-ФАЛАНГОВИЙ СУГЛОБ СЕРЕДНЬОГО
       MIDDLE_FINGER_PIP:   10         ПРОКСИМАЛЬНИЙ СУГЛОБ СЕРЕДНЬОГО
       MIDDLE_FINGER_DIP:   11         ДИСТАЛЬНИЙ СУГЛОБ СЕРЕДНЬОГО
       MIDDLE_FINGER_TIP:   12         КІНЧИК СЕРЕДНЬОГО ПАЛЬЦЯ
       RING_FINGER_MCP:     13         П'ЯСТНО-ФАЛАНГОВИЙ СУГЛОБ 
       RING_FINGER_PIP:     14         ПРОКСИМАЛЬНИЙ СУГЛОБ БЕЗІМЕННОГО
       RING_FINGER_DIP:     15         ДИСТАЛЬНИЙ СУГЛОБ БЕЗІМЕННОГО
       RING_FINGER_TIP:     16         КІНЧИК БЕЗІМЕННОГО ПАЛЬЦЯ
       PINKY_MCP:           17         П'ЯСТНО-ФАЛАНГОВИЙ СУГЛОБ МІЗИНЦЯ
       PINKY_PIP:           18         ПРОКСИМАЛЬНИЙ СУГЛОБ МІЗИНЦЯ
       PINKY_DIP:           19         ДИСТАЛЬНИЙ СУГЛОБ МІЗИНЦЯ
       PINKY_TIP:           20         КІНЧИК МІЗИНЦЯ
    ''')


####################

cap: cv2.VideoCapture | bool = False

def load_camera(url: str) -> None:
    """
    Opens a camera feed from the provided URL.
    Args:
        url (str) or 0: The URL of the remote camera or webcam to load.
    Raises:
        SystemExit: If the camera cannot be opened.
    """
    global cap
    cap = cv2.VideoCapture(url)
    if not cap.isOpened():
        exit("Cannot open camera")


def get_camera_frame() -> np.ndarray:
    """
    Captures a frame from the camera, flips it horizontally, and returns it.

    Returns:
        np.ndarray: The captured and flipped frame.
    """
    return cv2.flip(cap.read()[1], 1)


####################

gif_frames: list[np.array] = []
gif_index: int = 0

def load_gif(gif_path: str) -> None:
    """
    Loads frames from a GIF file and stores them in a list.
    Args:
        gif_path (str): The path to the GIF file to load.
    """
    global gif_frames
    with Image.open(gif_path) as gif:
        for frame in range(gif.n_frames):
            gif.seek(frame)
            gif_frames.append(cv2.cvtColor(np.array(gif.copy()), cv2.COLOR_RGBA2BGR))


def get_gif_frame() -> np.ndarray:
    """
    Retrieves the current frame from the loaded GIF and updates the frame index.
    Returns:
        np.ndarray: The current GIF frame.
    """
    global gif_frames, gif_index
    frame = gif_frames[gif_index]
    gif_index = (gif_index + 1) % len(gif_frames)
    return frame


####################

handsMp = mp.solutions.hands
hands = handsMp.Hands()
mpDraw = mp.solutions.drawing_utils

def findFingers(frame: np.ndarray) -> tuple[list, np.ndarray]:
    """
    Detects hand landmarks in the provided frame and draws them on the frame.
    Args:
        frame (np.ndarray): The input frame (BGR format) where hand detection is to be performed.
    Returns:
        tuple[list, np.ndarray]: The detected hand landmarks and the annotated frame.
    """
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handLms, handsMp.HAND_CONNECTIONS)
    return results.multi_hand_landmarks, frame


################################################################################

sourceType: str = ''

def load_source(path:str=0, gif: bool = False) -> None:
    """
    Loads a video source, either from a webcam or GIF file, based on the provided path.
    Args:
        path (str): The URL for the webcam or the path to the GIF file.
        gif (bool): Set to True if loading a GIF, False if loading a webcam feed.
    Example:
        load_source(): for webcam.
        load_source('http://192.168.1.2:5000'): for Android cam.
        load_source('test.gif', True): for local gif.
    """
    global sourceType
    if gif:
        load_gif(path)
        sourceType = 'gif'
    else:
        load_camera(path)
        sourceType = 'cam'


def get_frame() -> np.ndarray:
    """
    Retrieves a frame from the current video source (either webcam or GIF).
    Returns:
        np.ndarray: The current frame.
    """
    global sourceType
    if sourceType == 'cam':
        return get_camera_frame()
    if sourceType == 'gif':
        return get_gif_frame()


################################################################################


load_source('https://assets.mixkit.co/videos/4938/4938-720.mp4')
# load_source()
# load_source('hand.gif', gif=True)
# load_source('2hand.gif', gif=True)

while True:
    frame = get_frame()

    handLms, frame = findFingers(frame)

    if handLms:
        for handIndex, hand in enumerate(handLms):

            def get_finger_point_coords(finger) -> tuple[int, int]:
                h, w, _ = frame.shape
                return (int(finger.x * w), int(finger.y * h))
            
            forefinger = get_finger_point_coords(hand.landmark[8])
            thumb = get_finger_point_coords(hand.landmark[4])
            cv2.line(frame, forefinger, thumb, (255, 0, 0), 5)

            finger_distance = int(sqrt(pow(forefinger[0] - thumb[0], 2) + pow(forefinger[1] - thumb[1], 2)))
            cv2.putText(frame, str(finger_distance), thumb, cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

if not cap: cap.release()

cv2.destroyAllWindows()

```
