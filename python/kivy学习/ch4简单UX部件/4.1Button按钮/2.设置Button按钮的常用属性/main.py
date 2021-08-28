from typing import Text
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class MyBoxLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ButtonApp(App):
    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    ButtonApp().run()