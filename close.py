import random
from Body.speak import speak
import pyautogui as ui
from Data.Command.data import closedlg
def close():
    dld1 = random.choice(closedlg)
    speak(dld1)
    ui.hotkey("alt", "f4")

