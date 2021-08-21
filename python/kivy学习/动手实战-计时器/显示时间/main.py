from time import strftime
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

class ClockBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.on_start()
    
    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)

    def update_time(self,nap):
        self.ids.time_label_id.text = strftime('[b]%H[/b]:%M:%S')

class ClockApp(App):
    def build(self):
        return ClockBoxLayout()


if __name__ == '__main__':
    ClockApp().run()