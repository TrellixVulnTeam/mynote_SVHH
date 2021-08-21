from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class ClockBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ClockApp(App):
    def build(self):
        return ClockBoxLayout()


if __name__ == '__main__':
    ClockApp().run()