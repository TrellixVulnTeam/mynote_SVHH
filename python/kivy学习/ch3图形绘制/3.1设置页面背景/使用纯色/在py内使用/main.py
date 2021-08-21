from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color

class BoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(1,1,1,1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)

    
    def update_rect(self,*args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class BoxApp(App):
    def build(self):
        return BoxLayoutWidget()


if __name__ == '__main__':
    BoxApp().run()