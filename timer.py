from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty

class Timer(Label):
    done = BooleanProperty(False)

    def __init__(self, total, **kwargs):
        self.done = True
        self.total = total
        self.current = 0
        my_text = "Пройшло секунд: " + str(self.current)
        super().__init__(text=my_text)
    def start(self):
        Clock.schedule_interval(self.change, 1)

    def change(self, dt):
        self.current += 1
        my_text = "Пройшло секунд: " + str(self.current)
        super().__init__(text=my_text)
        if self.current >= self.total:
            self.done = True
            return False
        
