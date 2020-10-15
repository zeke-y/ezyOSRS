import cv2 as cv
from PIL import ImageGrab
import pyautogui
import numpy as np
from time import time

loop_time = time()
while True:

    img = ImageGrab.grab()
    img_np = np.array(img)
    frame = cv.cvtColor(img_np, cv.COLOR_RGB2BGR)
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
