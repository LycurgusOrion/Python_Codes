from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

import cx_Oracle as ox

conn = ox.connect("ADMIN/q2GWExrEGYz9JKM@db201902191526_low")


Builder.load_string("""
<whoscreen>:
    canvas:
        Rectangle:
            source: 'abc.jpg'
            pos: self.pos
            size: self.size
	Label:
		pos_hint:{"x":0,"y":0.4}
		text:"Choose User Type"
		font_size:30

	Button:
	    on_press: root.manager.current = 'retailerscreen'
	    pos_hint:{"x":0.35,"y":0.6}
	    text:"Retailer"

	Button:
	    pos_hint:{"x":0.35,"y":0.4}
	    text:"Executive"
	    on_press: root.manager.current = 'executivescreen'

	Button:
	    pos_hint:{"x":0.35,"y":0.2}
	    text:"Manufacturer"
	    on_press: root.manager.current = 'manufacturerscreen'

<retailerscreen>:

	uid:nameinput
	pass:passinput

    canvas:
        Rectangle:
            source: 'abc.jpg'
            pos: self.pos
            size: self.size       
    Button:
	    on_press: root.manager.current = 'whoscreen'
	    on_press: nameinput.text=""
	    on_press: passinput.text=""
		pos_hint:{"x":0,"top":1}
		text:"Back"
		
	Button:
		pos_hint:{"x":0.2,"y":0.1}
		text:"   Forgot\\nPassword"

	Button:
		pos_hint:{"x":0.5,"y":0.1}
		text:"Login"
		on_press:root.verify()
	 
		

	Label:
		pos_hint:{"x":-0.2,"y":0.2}
		text:"Username"

	Label:
		pos_hint:{"x":-0.2,"y":0}
		text:"Password"
	TextInput:
		id: nameinput
		size_hint: (.2, None)
		height: 30
		pos_hint:{"x":0.5,"y":0.67}
		multiline:False

	TextInput:
		id: passinput
		size_hint: (.2, None)
		height: 30
		pos_hint:{"x":0.5,"y":0.47}
		multiline:False
		password:True

<executivescreen>:
    canvas:
        Rectangle:
            source: 'abc.jpg'
            pos: self.pos
            size: self.size       
    Button:
	    on_press: root.manager.current = 'whoscreen'
	    on_press:nameinput.text=""
	    on_press:passinput.text=""
		pos_hint:{"x":0,"top":1}
		text:"Back"
		
	Button:
		pos_hint:{"x":0.2,"y":0.1}
		text:"   Forgot\\nPassword"

	Button:
		pos_hint:{"x":0.5,"y":0.1}
		text:"Login"


	Label:
		pos_hint:{"x":-0.2,"y":0.2}
		text:"Username"

	Label:
		pos_hint:{"x":-0.2,"y":0}
		text:"Password"
	TextInput:
		id: nameinput
		size_hint: (.2, None)
		height: 30
		pos_hint:{"x":0.5,"y":0.67}
		multiline:False

	TextInput:
		id: passinput
		size_hint: (.2, None)
		height: 30
		pos_hint:{"x":0.5,"y":0.47}
		multiline:False
		password:True

<manufacturerscreen>:
    canvas:
        Rectangle:
            source: 'abc.jpg'
            pos: self.pos
            size: self.size       
    Button:
	    on_press: root.manager.current = 'whoscreen'
	    on_press:nameinput.text=""
	    on_press:passinput.text=""
		pos_hint:{"x":0,"top":1}
		text:"Back"
		
	Button:
		pos_hint:{"x":0.2,"y":0.1}
		text:"   Forgot\\nPassword"

	Button:
		pos_hint:{"x":0.5,"y":0.1}
		text:"Login"
	 

	Label:
		pos_hint:{"x":-0.2,"y":0.2}
		text:"Username"

	Label:
		pos_hint:{"x":-0.2,"y":0}
		text:"Password"
	TextInput:
		id: nameinput
		size_hint: (.2, None)
		height: 30
		pos_hint:{"x":0.5,"y":0.67}
		multiline:False

	TextInput:
		id: passinput
		size_hint: (.2, None)
		height: 30
		pos_hint:{"x":0.5,"y":0.47}
		multiline:False
		password:True
		
<Button>:
	color:1,1,1,1
	font_size:16
	size_hint:0.3,0.1
""")

class whoscreen(Screen):
    pass

class retailerscreen(Screen):

	uid = ObjectProperty()

	def verify(self):
		print(self.uid.text)


class executivescreen(Screen):
    pass


class manufacturerscreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(whoscreen(name='whoscreen'))
sm.add_widget(retailerscreen(name='retailerscreen'))
sm.add_widget(executivescreen(name='executivescreen'))
sm.add_widget(manufacturerscreen(name='manufacturerscreen'))


class TestApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()
