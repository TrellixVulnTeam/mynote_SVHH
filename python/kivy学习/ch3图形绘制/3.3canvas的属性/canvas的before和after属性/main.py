from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class RelativeWidget(RelativeLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

class CanvasApp(App):
    def build(self):
        return RelativeWidget()

if __name__ =='__main__':
    CanvasApp().run()