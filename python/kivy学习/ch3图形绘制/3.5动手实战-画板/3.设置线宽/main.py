from kivy.app import App
from kivy.graphics import Line, Color
from kivy.uix.widget import Widget

from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.togglebutton import ToggleButton
from kivy.utils import get_color_from_hex


class DrawCanvasWidget(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        # 默认划线的颜色
        self.canvas.add(Color(rgb=[0,0,0]))
        self.line_width = 2

    def on_touch_down(self,touch):
        if Widget.on_touch_down(self,touch):
            return
        with self.canvas:
            touch.ud['current_line'] = Line(points=(touch.x,touch.y),width=self.line_width)

    def on_touch_move(self,touch):
        if 'current_line' in touch.ud:
            touch.ud['current_line'].points += (touch.x,touch.y)
    # 增加该方法改变颜色
    def change_color(self,new_color):
        self.canvas.add(Color(*new_color))
    
    #增加该方法，改变线宽度
    def change_line_width(self,width="Normal"):
        lines = {"Thin":1,"Normal":2,"Thick":4}
        self.line_width = lines[width]


class PaintApp(App):
    def build(self):
        self.draw_canvas_widget = DrawCanvasWidget()

        return self.draw_canvas_widget  # 返回root控件

if __name__ == "__main__":
    PaintApp().run()