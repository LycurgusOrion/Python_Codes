import pyautogui as pg
import time
import config

pg.FAILSAFE = True

pg.PAUSE = 0.1

time.sleep(5)

# Start Chrome
pg.hotkey("ctrl", "shift", "alt", "c")
time.sleep(5)
pg.hotkey("win", "up")
pg.hotkey("ctrl", "l")
pg.typewrite(config.YOUTUBE)
pg.press("enter")
time.sleep(5)
pg.click(300, 230)

pg.press(["tab", "tab"])

# Open the first ten videos
for i in range(9):
	pg.hotkey("ctrl", "enter")
	pg.press(["tab", "tab", "tab"])

time.sleep(5)

pg.hotkey("win", "d")
pg.hotkey("ctrl", "shift", "alt", "v")
time.sleep(5)
pg.hotkey("win", "up")
