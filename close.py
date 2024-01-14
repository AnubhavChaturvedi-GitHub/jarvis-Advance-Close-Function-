import random
from Body.Speak import SPEAK
import pyautogui as ui
from Data.Command.data import closedlg
def close():
    dld1 = random.choice(closedlg)
    SPEAK(dld1)
    ui.hotkey("alt", "f4")
