from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class ScaleBoxLayoutWidget(BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

class ScaleApp(App):
    def build(self):
        return ScaleBoxLayoutWidget()

if __name__ =='__main__':
    ScaleApp().run()