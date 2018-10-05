import tkinter as tk
import silentEmail
from tkinter import filedialog


class QuickMail:

	def __init__(self, root):

		root.title("Quick Mail v0.0.1")
		root.resizable(False, False)

		self.filename = ""
		self.password = ""

		self.label_0 = tk.Label(root, text="From").grid(
			row=0,
			column=0,
			sticky=tk.E
		)
		self.label_1 = tk.Label(root, text="To").grid(
			row=1,
			column=0,
			sticky=tk.E
		)
		self.label_2 = tk.Label(root, text="Subject").grid(
			row=2,
			column=0,
			sticky=tk.E
		)
		self.label_3 = tk.Label(root, text="Message").grid(
			row=3,
			column=0,
			sticky=tk.E
		)

		self.email_from_addr = tk.Entry(root, width=40)
		self.email_from_addr.grid(row=0, column=1)

		self.email_to_addr = tk.Entry(root, width=40)
		self.email_to_addr.grid(row=1, column=1)

		self.subject = tk.Entry(root, width=40)
		self.subject.grid(row=2, column=1)

		self.message = tk.Text(root, width=30, height=8)
		self.message.grid(row=3, column=1)

		self.a_button = tk.Button(
			root,
			text="Attach File",
			command=self.attach_file
		).grid(
			row=4,
			column=0 
		)

		self.send = tk.Button(
			root, text="Send", command=self.send_email, width=33)
		self.send.grid(row=4, column=1)

		self.screenshot = tk.Button(
			root, text="Take a screenshot", width=43)
		self.screenshot.grid(row=5, columnspan=2)
		self.screenshot.bind("<ButtonRelease-1>", self.grab_ss)

	def grab_ss(self, event):
		self.filename = silentEmail.take_ss()
		text = self.filename + " Captured and attached successfully"
		silentEmail.pg.alert(text=text, title="Success", button="Enjoy")

	def attach_file(self):
		self.filename = filedialog.askopenfilename()

	def send_email(self):

		if self.filename == "":
			check = silentEmail.pg.confirm(
				text="Send Mail Without Attachment?", title="Please Confirm", buttons=["Yeahhhh", "Noooo"])
			if check == "Noooo":
				self.attach_file()
			else:
				self.filename = "None"

		if self.email_from_addr.get() != silentEmail.config.EMAIL_ADDRESS:
			self.password = silentEmail.pg.password(text='Enter EMail Password',
													title='Password Prompt', default='', mask='#'
													)
			x = silentEmail.attach_and_mail(self.email_from_addr.get(), self.email_to_addr.get(),
											self.password, self.subject.get(),
											self.message.get("1.0", tk.END), self.filename)
		else:
			x = silentEmail.attach_and_mail(silentEmail.config.EMAIL_ADDRESS, self.email_to_addr.get(),
											silentEmail.config.PASSWORD, self.subject.get(),
											self.message.get("1.0", tk.END), self.filename)

		if x == 0:
			silentEmail.pg.alert(
				text="E-Mail Successfully sent", title="Success", button="Hell Yeah!")
		else:
			text = "Error: " + str(x)
			silentEmail.pg.alert(
				text=text, title="Error Sending Mail", button="Sed Life")


def Main():

	root = tk.Tk()

	gui = QuickMail(root)

	root.mainloop()


if __name__ == "__main__":
	Main()
