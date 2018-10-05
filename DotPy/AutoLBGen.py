from pyautogui import hotkey, press, typewrite, keyDown, keyUp
from time import sleep, time

import pyautogui


def Main():

	pyautogui.PAUSE = 0.1

	# Start Delay only for debugging
	sleep(5)

	# Switch to formatter and cleanup
	keyDown("alt")
	press("tab")
	keyUp("alt")
	
	# Navigate to the first sheet
	for i in range(6):
		hotkey("ctrl", "pageup")

	# Clean the second sheet
	hotkey("ctrl", "pagedown")
	hotkey("ctrl", "home")
	press("down")
	# Delete Existing content
	press("f8")
	hotkey("ctrl", "end")
	press("delete")
	hotkey("ctrl", "home")

	# Navigate to Survey data sheet
	for i in range(5):
		hotkey("ctrl", "pagedown")
	
	hotkey("ctrl", "home")
	press("down")

	# Delete Existing content
	press("f8")
	hotkey("ctrl", "end")
	press("delete")
	hotkey("ctrl", "home")

	# Switch to CSV
	keyDown("alt")
	press("tab")
	keyUp("alt")

	# Starting with the CSV File
	hotkey("ctrl", "home")

	hotkey("ctrl", "down")
	press("f8")
	hotkey("ctrl", "end")
	hotkey("ctrl", "c")
	hotkey("ctrl", "home")
	hotkey("ctrl", "down")
	press("down")
	hotkey("ctrl", "v")
	hotkey("ctrl", "home")

	# Enter extended selection mode
	press("f8")
	hotkey("ctrl", "down")

	# Insert Column to the left
	hotkey("ctrl", "+")
	press("enter")
	hotkey("ctrl", "home")
	
	# Write and calculate the HOP
	typewrite("HOP")
	press("enter")

	# Copy and paste the Site ID here
	press("right")
	press("f8")
	hotkey("ctrl", "down")
	hotkey("ctrl", "c")
	press("left")
	hotkey("ctrl", "v")
	press("left")

	# Type in the formula
	typewrite("=CONCATENATE(B2, \"-\", C2)")
	press("enter")

	# Fill the above formula 
	# in all the cells
	press("up")
	press("f8")
	hotkey("ctrl", "down")
	hotkey("ctrl", "d")
	hotkey("ctrl", "home")
	hotkey("ctrl", "down")
	press("f8")
	hotkey("ctrl", "end")
	press("f8")
	press("delete")
	hotkey("ctrl", "home")
	press("down")
	
	# Copy The Contents
	press("f8")
	hotkey("ctrl", "end")
	hotkey("ctrl", "c")
	
	# Swith to LB Formatter
	keyDown("alt")
	press("tab")
	keyUp("alt")
	
	# Navigate to the first sheet
	for i in range(6):
		hotkey("ctrl", "pageup")
	
	# Paste in the second sheet
	hotkey("ctrl", "pagedown")
	hotkey("ctrl", "home")
	press("down")
	# Paste
	hotkey("ctrl", "v")

	# Switch to LOS Tracker
	keyDown("alt")
	press("tab")
	press("tab")
	keyUp("alt")

	# Append a row at the end
	hotkey("ctrl", "home")

	hotkey("ctrl", "down")
	press("f8")
	hotkey("ctrl", "end")
	hotkey("ctrl", "c")
	hotkey("ctrl", "home")
	hotkey("ctrl", "down")
	press("down")
	hotkey("ctrl", "v")
	hotkey("ctrl", "home")
	
	# Copy from the tracker
	press("down")
	press("f8")
	hotkey("ctrl", "end")
	press("f8")
	hotkey("ctrl", "c")
	
	# Switch to the LB formatter
	keyDown("alt")
	press("tab")
	keyUp("alt")

	# Navigate to Survey data sheet
	for i in range(5):
		hotkey("ctrl", "pagedown")

	# pyautogui.PAUSE = 2
	# Paste the contents
	hotkey("ctrl", "home")
	press("down")
	# Paste
	hotkey("ctrl", "v")
	press("left")


	# Go to the first FAR END
	press("right", 30)
	press("f8")
	press("right", 10)
	hotkey("ctrl", "down")
	press("f8")
	hotkey("ctrl", "c")

	# Go to the NEAR END and paste below
	press("left", 11)
	hotkey("ctrl", "down")
	press("down")
	hotkey("ctrl", "v")

	sleep(0.1)
	press("right")
	hotkey("ctrl", "home")
	press("down")

	# Go to the second FAR END
	hotkey("ctrl", "right")
	press("left", 17)
	press("f8")
	press("right", 10)
	hotkey("ctrl", "down")
	press("f8")
	hotkey("ctrl", "c")
	
	# Go to the NEAR END and paste below
	press("left", 22)
	hotkey("ctrl", "down")
	press("down")
	hotkey("ctrl", "v")
	
	press("right")
	hotkey("ctrl", "s")

	# Navigate to the first sheet
	for i in range(6):
		hotkey("ctrl", "pageup")

if __name__ == "__main__":
	Main()
