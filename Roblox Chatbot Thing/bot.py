#Libraries, DO NOT TOUCH AT ALL
import time
import random
import pyautogui

#You can make these strings whatever you want and you can add more.
choosable_text = [
    "I'm saving this robux to help gear up the BOIS.",
    "All of this robux is going towards my friends.",
    "This robux will help me and the bois in the games we play.",
]
#Change chosen to how long you choosable_text array is. You can change the other two if you want.
chosen = random.randint(1, 3)
waitTime = random.randint(1, 10)
cooldown = 1

#Do not edit code from here on out.
while True:
    time.sleep(waitTime)
    pyautogui.leftClick()
    time.sleep(0.1)
    pyautogui.press("/", 1)
    pyautogui.typewrite(choosable_text[chosen])
    pyautogui.press("enter", 1)
    time.sleep(cooldown)