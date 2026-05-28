from kivy.app import App
from kivy.uix.button import Button

class Jarvis(App):
    def build(self):
        return Button(text="Jarvis Online")

Jarvis().run()