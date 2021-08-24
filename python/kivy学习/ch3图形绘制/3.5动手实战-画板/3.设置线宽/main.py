from kivy.app import App
from kivy.graphics import Line, Color
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex

# 运行不成功，不知道哪里出问题了
class DrawCanvasWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # self.canvas.add(Color(rgb=[0,0,0]))
        self.canvas.add(Color(rgb=get_color_from_hex('#ecad9e')))
        self.line_width = self.change_line_width('Normal')
        # self.line_width = 3


    def change_line_width(self, width='Normal'):
        lines = {'Thin':1,'Normal':2,'Thick':4}
        self.line_width = lines[width]
        # return self.line_width

    def on_touch_down(self, touch):
        if Widget.on_touch_down(self,touch):
            return
        with self.canvas:
            touch.ud['current_line'] = Line(points=(touch.x,touch.y),width=self.line_width)
    
    def on_touch_move(self, touch):
        if 'current_line' in touch.ud:
            touch.ud['current_line'].points += (touch.x,touch.y)


class PaintApp(App):
    def build(self):
        self.draw_canvas_widget = DrawCanvasWidget()
        return self.draw_canvas_widget


if __name__ == '__main__':
    PaintApp().run()