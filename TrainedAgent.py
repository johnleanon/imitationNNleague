import random
import time

from utils.getkeys import key_check
import pydirectinput
import keyboard
import time
import cv2
from utils.grabscreen import grab_screen
from utils.directkeys import PressKey, ReleaseKey, W, D, A
from fastai.vision.all import *

def label_func(x): return x.parent.name
learn_inf = load_learner("D:\GC/export.pkl")
print("loaded learner")

# Sleep time after actions
sleepy = 0.1

# Wait for me to push B to start.
keyboard.wait('B')
time.sleep(sleepy)

# Hold down W no matter what!

# Randomly pick action then sleep.
# 0 do nothing release everything ( except W )
# 1 hold left
# 2 hold right
# 3 Press Jump

while True:

    image = grab_screen(region=(1, 1, 1920, 1080))
    image = cv2.resize(image,(84,84))
    cv2.imshow("Fall", image)
    # cv2.imshow("Fall", image)
    # cv2.waitKey(1)
    start_time = time.time()
    result = learn_inf.predict(image)
    action = result[0]
    #print(result[2][0].item(), result[2][1].item(), result[2][2].item(), result[2][3].item())

    #action = random.randint(0,3)
    
    if action == "W" or result[2][0]>.1:
        print(f"W! - {result[1]}")
        keyboard.press("w")
        keyboard.release("a")
        keyboard.release("d")
        keyboard.release("s")
        time.sleep(sleepy)

    if action == "Nothing":
        #print("Doing nothing....")
        keyboard.release("w")
        keyboard.release("a")
        keyboard.release("d")
        keyboard.release("s")
        time.sleep(sleepy)

    elif action == "A":
        print(f"A! - {result[1]}")
        keyboard.press("a")
        keyboard.release("w")
        keyboard.release("d")
        keyboard.release("s")
        time.sleep(sleepy)

    elif action == "S":
        print(f"S! - {result[1]}")
        keyboard.press("s")
        keyboard.release("w")
        keyboard.release("d")
        keyboard.release("a")
        time.sleep(sleepy)

    elif action == "D":
        print(f"D! - {result[1]}")
        keyboard.press("d")
        keyboard.release("w")
        keyboard.release("s")
        keyboard.release("a")
        time.sleep(sleepy)

    # End simulation by hitting h
    keys = key_check()
    if keys == "H":
        break

keyboard.release('W')