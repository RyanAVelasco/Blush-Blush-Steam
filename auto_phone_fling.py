import os
import pyautogui as p
import time
import colored
from colored import stylize

Images = {
    "New": os.path.join("images", "phone_fling_new_icon.png"),
    "Reply": os.path.join("images", "phone_fling_reply.png"),
    "Icon": os.path.join("images", "phone_fling_reply_icon.png"),
    "Reset": os.path.join("images", "phone_fling_reset.png"),
    "Back": os.path.join("images", "phone_fling_back_button.png"),
    "Nxt_Message": os.path.join("images", "phone_fling_next_message_timer.png")
}

while True:

    if p.locateOnScreen(Images["New"]):
        p.moveTo(p.locateOnScreen(Images["New"]))
        p.click()

    elif p.locateOnScreen(Images["Icon"]):
        p.moveTo(p.locateOnScreen(Images["Icon"]))
        p.click()

    if p.locateOnScreen(Images["Reply"]):
        p.click(p.locateOnScreen(Images["Reply"]))
        p.click()

    if p.locateOnScreen(Images["Back"]):
        p.click(p.locateOnScreen(Images["Back"]))
