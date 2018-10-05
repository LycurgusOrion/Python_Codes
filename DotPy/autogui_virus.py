import pyautogui as pg
import random as r
import config

maxx, maxy = pg.size()

while True:
	rx = r.randint(1, maxx)
	ry = r.randint(1, maxy)
	rk = r.randint(0, len(config.KEYS))
	try:
		pg.press(config.KEYS[rk])
		if rx > ry:
			pg.moveTo(rx, ry)
		elif rx < ry:
			pg.click(rx, ry, clicks=int(ry/rx))
		else:
			pg.click(rx, ry, button="right")
	except:
		continue
