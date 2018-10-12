import pyautogui as pg
import time

time.sleep(2)

pg.PAUSE = 0.1

pg.hotkey("alt", "tab")
pg.hotkey("ctrl", "t")
pg.hotkey("ctrl", "l")
pg.typewrite("Python is fun!")
pg.press("enter")
