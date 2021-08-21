from time import strftime
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

class ClockBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.timing_flag = False
        self.timing_seconds = 0
        self.on_start()
    
    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)

    # 这个参数nap没看懂
    def update_time(self,nap):
        if self.timing_flag:
            self.timing_seconds += nap

        self.ids.time_label_id.text = strftime('[b]%H[/b]:%M:%S')

        m, s = divmod(self.timing_seconds, 60)

        self.ids.stopwatch.text = ('%02d:%02d.[size=30]%02d[/size]' % (int(m), int(s), int(s*100 % 100)))
    
    def start_or_stop(self):
        if self.timing_flag:
            self.ids.start_stop_button_id.text = 'Start'
        else:
            self.ids.start_stop_button_id.text = 'Stop'
        # self.ids.start_stop_button_id.text = 'Start' if self.timing_flag else 'Stop'
        self.timing_flag = not self.timing_flag


class ClockApp(App):
    def build(self):
        return ClockBoxLayout()


if __name__ == '__main__':
    ClockApp().run()