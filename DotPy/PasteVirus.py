import pyautogui as pg
import random as r
import config
import time

pg.PAUSE = 0.5
pg.FAILSAFE = False

maxx, maxy = pg.size()

# Open the pendrive
pg.hotkey("win", "e")
pg.press(config.USB_CHAR)
pg.press("enter")
pg.press(config.FNAME_CHAR)

# Copy the file
pg.hotkey("ctrl", "c")

# Open the startup folder
pg.hotkey("ctrl", "l")
pg.typewrite(config.STARTUP_LOCATION)
pg.press("enter")
pg.hotkey("win", "up")

# Focus the window
pg.click(maxx/2, maxy/2)

# Paste the file
pg.hotkey("ctrl", "v")
pg.press("enter")
time.sleep(2)

# Open the file
pg.press("enter")

# Focus on the File
# Explorer and close it
pg.click(maxx/2, 0)
pg.hotkey("alt", "f4")
