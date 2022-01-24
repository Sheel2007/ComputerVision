import cv2
from PIL import ImageGrab
import numpy as np
import keyboard
import pyautogui
import time
#this program only works in split screen with pycharm on the right
BOX_CORDS = (970, 331, 1860, 510)
BOX_LEFT, BOX_TOP, BOX_RIGHT, BOX_BOTTOM = BOX_CORDS
OBSTACLE_COLOR = (83, 83, 83)
GROUND_OBSTALCE_Y = 480
GROUND_DELTA = GROUND_OBSTALCE_Y - BOX_TOP
RED = (255, 0, 0)
GREEN = (0, 255, 0)
OBS_TOCOLOR_HEIGHT = 10


def jump():
    pyautogui.keyDown('space')
    time.sleep(0.02)
    pyautogui.keyUp('space')


def get_in_front_range():
    return 160, 260


def get_ground_obs(img):
    ground = img[GROUND_DELTA]
    obs = [i for i, pix in enumerate(ground) if (pix == OBSTACLE_COLOR).all()]
    return obs[5:]  # get rid off feet obstacle


def colors_obs(img, obs):
    for ind in obs:
        for i in range(OBS_TOCOLOR_HEIGHT):
            img[GROUND_DELTA + i][ind] = RED


while True:
    img = ImageGrab.grab(bbox=BOX_CORDS)  # left_x, top_y, right_x, bottom_y
    img = np.array(img)
    obs = get_ground_obs(img)

    front_start, front_end = get_in_front_range()
    for x in obs:
        if front_start <= x:
            if x <= front_end:
                jump()
            break

    colors_obs(img, obs)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = cv2.rectangle(img, (front_start, GROUND_DELTA), (front_end, GROUND_DELTA + 10), GREEN)
    cv2.imshow('img', img)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
