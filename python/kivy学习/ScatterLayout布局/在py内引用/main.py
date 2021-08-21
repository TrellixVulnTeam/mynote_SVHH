from kivy.app import App
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.graphics import Rectangle, Color

class ScatterLayoutWidget(ScatterLayout):
    pass

class BoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(pos=self.pos,size=self.size)
            self.bind(pos=self.update_rect,size=self.update_rect)

        scatter_layout = ScatterLayoutWidget()

        image = AsyncImage(source='F:\本机照片20210606\IMG_20180524_152522.jpg')
        scatter_layout.add_widget(image)
        self.add_widget(scatter_layout)

    def update_rect(self,*args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class ScatterApp(App):
    def build(self):
        return BoxLayoutWidget()

if __name__ == '__main__':
    ScatterApp().run()