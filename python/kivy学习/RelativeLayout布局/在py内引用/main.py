from kivy import app
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color

class MyButton(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.font_size = 20
        self.size_hint = [0.2, 0.2]


class RelativeLayoutWidget(RelativeLayout):
    pass

class BoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(1,1,1,1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)

        
        relative_layout = RelativeLayoutWidget()

        bt0 = MyButton(text='bt0',pos_hint={'right':1, 'top': 1},background_color=(0.1, 0.5, 0.6, 1))

        bt1 = MyButton(text='bt1',pos_hint={'x':1, 'top': 1},background_color=(1, 0, 0, 1))

        bt_relative = MyButton(text='Relative',pos_hint={'center_x': .5, 'center_y': .5},background_color=(0.4, 0.5, 0.6, 1))

        bt2 = MyButton(text='bt2',pos_hint={'x':0, 'y': 0},background_color=(0, 0, 1, 1))

        bt3 = MyButton(text='bt3',pos_hint={'right':1, 'y': 0},background_color=(0.8, 0.9, 0.2, 1))

        for i in [bt0, bt1, bt_relative, bt2, bt3]:
            relative_layout.add_widget(i)

        
        self.add_widget(BoxLayout())

        self.add_widget(relative_layout)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class RelativeApp(App):
    def build(self):
        return BoxLayoutWidget()

if __name__ == '__main__':
    RelativeApp().run()