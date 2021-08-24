from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class TranslateBoxLayoutWidget(BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

class TranslateApp(App):
    def build(self):
        return TranslateBoxLayoutWidget()

if __name__ =='__main__':
    TranslateApp().run()