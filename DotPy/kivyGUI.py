import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.button import Label

class HelloKivy(App):

	def build(self):
		return Label(text="Hello Kivy")

def Main():

	helloKivy = HelloKivy()

	helloKivy.run()

if __name__ == "__main__":
	Main()
