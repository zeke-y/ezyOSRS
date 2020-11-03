import cv2 as cv
from PIL import Image
import pyautogui
import numpy as np
import time

pyautogui.press('winleft')
time.sleep(1)
pyautogui.typewrite('runelite')
time.sleep(1)
pyautogui.press('enter')
time.sleep(15)
# take screenshot
loginscr_needle = pyautogui.screenshot()
loginscr_needle = cv.cvtColor(np.array(loginscr_needle), cv.COLOR_RGB2BGR)
cv.imwrite("/home/zekey/Coding/Projects/OSRSbot/ATTEMPT2/images/in_memory_to_disk.png", loginscr_needle)
print("loginscr_needle complete")

loginscr_haystack = Image.open("/home/zekey/Coding/Projects/OSRSbot/ATTEMPT2/images/existinguser.png")
loginscr_haystack = cv.cvtColor(np.array(loginscr_haystack), cv.COLOR_RGB2BGR)
cv.imwrite("/home/zekey/Coding/Projects/OSRSbot/ATTEMPT2/images/existinguser.png", loginscr_haystack)

print("loginscr_haystack complete")

result = cv.matchTemplate(loginscr_haystack, loginscr_needle, cv.TM_CCOEFF_NORMED)
print("matched template")

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print("best match top left position: %s" % str(max_loc))
print("best match confidence: %s" % max_val)

threshold = 0.8
if max_val >= threshold:
    print('Found needle.')

    # get dimensions of the needle image
    needle_w = loginscr_needle.shape[1]
    needle_h = loginscr_needle.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    cv.rectangle(loginscr_haystack, top_left, bottom_right,
                 color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

    pyautogui.moveTo(max_loc[0] + 80, max_loc[1] + 30, duration=1)
    pyautogui.leftClick()
    pyautogui.typewrite("PASSWORD")
    pyautogui.moveTo(max_loc[0] - 80, max_loc[1] + 40, duration=1)
    pyautogui.leftClick()
    time.sleep(7)
    pyautogui.leftClick()


else:
    print('Needle not found.')
