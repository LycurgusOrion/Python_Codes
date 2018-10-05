# import silentEmail

# # import tkinter as tk

# # class TextTest():

# # 	def __init__(self):
		
# # 		self.label = tk.Label(root, text="Text").grid(
# #                     row=0,
# #                     column=0,
# #                     sticky=tk.E
# #                 )

# # 		self.t = tk.Text(root, width=40, height=10)
# # 		self.t.grid(row=0, column=1)

# # 		self.b = tk.Button(root, text="Print", command=self.print_text).grid(
# # 			row=1,
# # 			columnspan=2,
# # 		)
	
# # 	def print_text(self):
# # 		msg = self.t.get("1.0", tk.END)
# # 		print(msg.strip())


# # root = tk.Tk()
# # root.title("Helooz frandzzz")
# # x = TextTest()

# # root.mainloop()

# # def capture():
# silentEmail.time.sleep(silentEmail.config.SS_DELAY)
# silentEmail.pg.keyDown("win")
# silentEmail.pg.press("down")
# silentEmail.time.sleep(silentEmail.config.SS_DELAY)
# filename = silentEmail.capture_ss()
# silentEmail.time.sleep(silentEmail.config.SS_DELAY)
# silentEmail.pg.press("up")
# silentEmail.pg.keyUp("win")
# print(filename)

import pyautogui as py
import time

time.sleep(5)
py.press("pgdown")