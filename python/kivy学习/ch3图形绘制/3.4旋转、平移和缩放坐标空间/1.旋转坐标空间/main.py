from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class RotateGridLayoutWidght(GridLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

class RotateApp(App):
    def build(self):
        return RotateGridLayoutWidght()

if __name__ =='__main__':
    RotateApp().run()