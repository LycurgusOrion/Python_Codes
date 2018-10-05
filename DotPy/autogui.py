import pyautogui as pag
import tkinter as tk
import time

def draw(distance, startx, starty):
	pag.moveTo(startx, starty)
	while distance > 0:
		pag.dragRel(distance, 0)   # move right
		distance -= 5
		pag.dragRel(0, distance)   # move down
		pag.dragRel(-distance, 0)  # move left
		distance -= 5
		pag.dragRel(0, -distance)  # move up
	return pag.position()

time.sleep(3)

sw, sh = pag.size()

distance = 200

# Open Paint
pag.moveTo(15, 155)
pag.click()

# Draw the spiral
curr_x, curr_y = draw(distance=200, startx=15, starty=155)
curr_x, curr_y = draw(distance=100, startx=curr_x, starty=curr_y)
curr_x, curr_y = draw(distance=200, startx=curr_x, starty=curr_y)
curr_x, curr_y = draw(distance=50, startx=curr_x, starty=curr_y)

# root = tk.Tk()
# label = tk.Label(root, text=str(pag.position()))
# label.pack()

# def update_label():
# 	label["text"] = str(pag.position())
# 	root.after(1, update_label)

# root.after(1, update_label)
# root.mainloop()

# i=0
# while True:
# 	if i%2 == 0:
# 		pag.moveRel(100, 100, duration=2, tween=pag.easeInOutQuad)
# 	else:
# 		pag.moveRel(-100, -100, duration=2, tween=pag.easeInOutQuad)

# 	i+=1

# pag.click()
