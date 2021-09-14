from kivymd.app import MDApp
from kivy.uix.textinput import TextInput

class DemoApp(MDApp):
    def build(self):
        textinput = TextInput(text='Hello world')
        return  textinput

DemoApp().run()
