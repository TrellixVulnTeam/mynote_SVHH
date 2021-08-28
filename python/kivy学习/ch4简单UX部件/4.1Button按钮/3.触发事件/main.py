from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class ButtonFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def press_button(self,arg):
        print('press_button is running%s'%arg)

    def release_button(self):
        print('release_button is running')

class ButtonApp(App):
    def build(self):
        return ButtonFloatLayout()


if __name__ == '__main__':
    ButtonApp().run()