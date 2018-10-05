import smtplib
import config
import tkinter as tk

class EMail:
	
	def __init__(self, root):
		self.label_1 = tk.Label(root, text="Email To").grid(row=0, column=0, sticky=tk.E)
		self.label_3 = tk.Label(root, text="Subject").grid(row=1, column=0, sticky=tk.E)
		self.label_2 = tk.Label(root, text="Message").grid(row=2, column=0, sticky=tk.E)

		self.email_to_addr = tk.Entry(root)
		self.email_to_addr.grid(row=0, column=1)

		self.subject = tk.Entry(root)
		self.subject.grid(row=1, column=1)	
		
		self.message = tk.Entry(root)
		self.message.grid(row=2, column=1)

		self.send = tk.Button(root, text="SEND", command=self.send_email)
		self.send.grid(row=3, columnspan=2)


	def send_email(self):

		print(self.email_to_addr.get(), self.message.get(), self.subject.get())
		print(config.EMAIL_ADDRESS, config.PASSWORD)

		try:
			server = smtplib.SMTP("smtp.gmail.com:587")
			server.ehlo()
			server.starttls()
			server.login(config.EMAIL_ADDRESS, config.PASSWORD)
			server.sendmail(config.EMAIL_ADDRESS, self.email_to_addr.get(), self.message.get())
			server.sendmail()
			print("Success")
		except:
			print("Error")

def Main():
	root = tk.Tk()
	email = EMail.send_email()
	root.mainloop()

if __name__ == "__main__":
	Main()
		
