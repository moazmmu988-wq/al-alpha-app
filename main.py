from kivy.app import App
from kivy.uix.label import Label

class AlAlphaApp(App):
    def build(self):
        return Label(text='مرحباً بك يا مولاي في المساعد ألفا 🛸⚡')

if __name__ == '__main__':
    AlAlphaApp().run()
