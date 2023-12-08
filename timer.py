from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty

class Timer(Label): # клас для таймера
    done = BooleanProperty(False) # флажок для таймера

    def __init__(self, total, **kwargs):
        self.done = False
        self.total = total # кількість секунд в таймері
        self.current = 0 # лічильник секунд
        my_text = "Пройшло секунд: " + str(self.current) # текст віджету таймера
        super().__init__(text=my_text) # виклик конструктора класу

    def start(self): # метод запуску таймера
        Clock.schedule_interval(self.change, 1) # запуск метода селф чендж

    def change(self, dt): # функція обробник
        self.current += 1 # збільшуємо секунди
        my_text = "Пройшло секунд: " + str(self.current) # міняємо текст
        super().__init__(text=my_text)
        if self.current >= self.total: # умова зупинки таймера
            self.done = True # міняємо властивість
            return False # зупиняємо таймер
        
