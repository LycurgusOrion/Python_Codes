import pyautogui as pg
import time

time.sleep(2)

pg.PAUSE = 0.1

# Display tree of current directory
pg.hotkey("ctrl", "alt", "t")
time.sleep(4)
pg.typewrite("tree")
pg.press("enter")

time.sleep(6)

# Select the tree and copy it
pg.keyDown("ctrl")
pg.keyDown("shift")
pg.keyDown("up")
pg.keyUp("up")
pg.keyUp("shift")
pg.keyUp("ctrl")