import pyautogui as py
import time


def copy():
	py.hotkey("ctrl", "c")


def paste():
	py.hotkey("ctrl", "v")


def switch():
	py.hotkey("alt", "tab")
	py.hotkey("ctrl", "home")


def switchAndCopy(x, y):
	py.press("pagedown")
	py.doubleClick(x, y)
	copy()
	switch()


def press(key, times):
	for i in range(times):
		
		py.press(key)



def Main():
	
	py.PAUSE = 0.145

	# Assign the screen coordinates
	amsl1x, amsl1y = 606, 541
	amsl2x, amsl2y = 975, 541

	lat1x, lat1y = 618, 373
	long1x, long1y = 618, 429

	lat2x, lat2y = 984, 373
	long2x, long2y = 984, 429

	blankx, blanky = 621, 221
	listx, listy = 888, 222

	# Select the first site
	py.click(listx, listy)
	py.press("home")
	py.press("enter")
	py.click(blankx, blanky)

	# Copy Lat and Paste
	switchAndCopy(lat1x, lat1y)
	press("right", 2)
	paste()
	py.press("down")
	paste()
	py.press("down")
	paste()

	# Copy AMSL and Paste
	switch()
	switchAndCopy(amsl1x, amsl1y)
	press("right", 2)
	press("down", 4)
	paste()

	# Copy FarEnd AMSL and Paste
	switch()
	switchAndCopy(amsl2x, amsl2y)
	py.hotkey("ctrl", "right")
	py.press("right")
	paste()

	# Copy Longitude and Paste
	switch()
	switchAndCopy(long1x, long1y)
	press("right", 3)
	paste()
	py.press("down")
	paste()
	py.press("down")
	paste()

	# Copy FarEnd Lat and Paste
	switch()
	switchAndCopy(lat2x, lat2y)
	press("right", 5)
	paste()

	# Copy FarEnd Longitude and Paste
	switch()
	switchAndCopy(long2x, long2y)
	press("right", 6)
	paste()

	# Select the second Site
	switch()
	py.click(listx, listy)
	py.press("down")
	py.press("enter")
	py.click(blankx, blanky)

	# Copy FarEnd Lat and Paste
	switchAndCopy(lat2x, lat2y)
	press("right", 5)
	py.press("down")
	paste()

	# Copy FarEnd Long and Paste
	switch()
	switchAndCopy(long2x, long2y)
	press("right", 6)
	py.press("down")
	paste()

	# Copy FarEnd AMSL and Paste
	switch()
	switchAndCopy(amsl2x, amsl2y)
	py.hotkey("ctrl", "right")
	py.press("down")
	paste()

	# Select the third Site
	switch()
	py.click(listx, listy)
	py.press("down")
	py.press("enter")
	py.click(blankx, blanky)

	# Copy FarEnd Lat and Paste
	switchAndCopy(lat2x, lat2y)
	press("right", 5)
	press("down", 2)
	paste()

	# Copy FarEnd Long and Paste
	switch()
	switchAndCopy(long2x, long2y)
	press("right", 6)
	press("down", 2)
	paste()

	# Copy FarEnd AMSL and Paste
	switch()
	switchAndCopy(amsl2x, amsl2y)
	py.hotkey("ctrl", "right")
	press("down", 2)
	paste()


if __name__ == "__main__":
	start_time = time.time()
	Main()
	print("Execution Time: " + str(time.time() - start_time))
