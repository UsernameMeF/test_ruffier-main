from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from instructions import *
from timer import Timer
from ruffier import test


#Window.clearcolor = (0, .10, .56, 1)
lbl_color = (.1, .32, .79, 1)
btn_color = (.1, .34, .65, 1)

name = ""
age = 0

p1 = 0
p2 = 0
p3 = 0

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

class IntrScr(Screen): # клас
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction, color=lbl_color, bold=True) # текст
        lbl_name = Label(text="Введіть ім'я:", halign="right", color=lbl_color, bold=True, font_size=25) # створюємо лабель
        self.input_name = TextInput(text="Максим", multiline = False) # робимо строку для тексту (типо кнопка)
        lbl_age = Label(text="Введіть вік:", halign="right", color=lbl_color, bold=True, font_size=25) # створюємо лабель
        self.input_age = TextInput(text="7+", multiline = False) # робимо строку для тексту (типо кнопка)

        self.btn = Button(text="Почати", size_hint=(.3, .1), pos_hint={'center_x': .5}, bold=True, background_color=btn_color) # створюємо лабель       
        self.btn.on_press = self.next # кнопка яка буде змінювати екран на другий

        line1 = BoxLayout(size_hint=(.8, None), height="30sp") # лінія для тексту
        line2 = BoxLayout(size_hint=(.8, None), height="30sp") # лінія для тексту

        line1.add_widget(lbl_name) # додаємо віджети
        line1.add_widget(self.input_name) # додаємо віджети

        line2.add_widget(lbl_age) # додаємо віджети
        line2.add_widget(self.input_age) # додаємо віджети

        main_line = BoxLayout(orientation="vertical", padding = 10, spacing=15) # мейн лінію робимо
        main_line.add_widget(instr)
        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.btn) # додаємо всі штуки які робили в 13-28 строках

        self.add_widget(main_line) # додаємо мейн лайн

    def next(self): # змінює екран + перевірка
        global name, age
        name = self.input_name.text
        age = check_int(self.input_age.text)
        if age <= 7 or age is False: 
            age = 7
            self.input_age.text = str(age)
        else:
            self.manager.current = "second"



class PulseScr(Screen): # клас
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        instr = Label(text=txt_test1, color=lbl_color, bold=True, font_size=25) # текст
        
        self.lbl_sec = Timer(15, color=lbl_color, bold=True) # Таймер
        self.lbl_sec.bind(done=self.end_timer)

        lbl_result = Label(text="Введіть результат:", halign="right", color=lbl_color, bold=True, font_size=25) # створюємо лабель
        self.input_result = TextInput(text="1", multiline = False) # робимо строку для тексту (типо кнопка)

        self.input_result.set_disabled(True) # БЛОКИРОВКА

        self.btn = Button(text="Почати", size_hint=(.3, .2), pos_hint={'center_x': .5}, bold=True, background_color=btn_color) # створюємо лабель       
        self.btn.on_press = self.next # кнопка яка буде змінювати екран на другий

        main_line = BoxLayout(orientation="vertical", padding = 10, spacing=15) # мейн лінію робимо
        main_line.add_widget(instr)
        main_line.add_widget(self.lbl_sec)
        line = BoxLayout(size_hint=(.8, None), height="30sp") # лінія для тексту
        line.add_widget(lbl_result)
        line.add_widget(self.input_result)
        main_line.add_widget(line)
        main_line.add_widget(self.btn)
        
        self.add_widget(main_line) # Добавляємо мейн лінію на екран (self)

    def end_timer(self, *args):
        self.next_screen = True
        self.input_result.set_disabled(False)
        self.btn.text = "Продовжити"



    def next(self): # змінює екран + перевірка
        global p1
        if not self.next_screen: 
            self.input_result.set_disabled(False)
            self.lbl_sec.start()
            
        else:
            p1 = check_int(self.input_result.text)
            if p1 is False or p1 <= 1:
                p1 = 0
                self.input_result.text = str(p1)
            else:
                self.manager.current = "third"


class SitsScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test2, color=lbl_color, bold=True, font_size=25) # текст

        self.sits = Label(text="Залишилось присідань: 30", color=lbl_color, bold=True)

        self.btn = Button(text="Почати", size_hint=(.3, .2), pos_hint={'center_x': .5}, bold=True, background_color=btn_color) # створюємо лабель       
        self.btn.on_press = self.next # кнопка яка буде змінювати екран на другий

        main_line = BoxLayout(orientation="vertical", padding = 10, spacing=15) # мейн лінію робимо
        main_line.add_widget(instr)
        main_line.add_widget(self.sits)
        main_line.add_widget(self.btn)


        self.add_widget(main_line)

    def next(self): # змінює екран
        self.manager.current = "fourth"

class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test3, color=lbl_color, bold=True, font_size=25) # текст
        lbl_pulse = Label(text="Рахуйте пульс", color=lbl_color, bold=True)
        self.lbl_sec = Label(text="Пройшло секунд: 0", color=lbl_color, bold=True)
        
        lbl_result = Label(text="Результат", halign="right", color=lbl_color, bold=True, font_size=25) # створюємо лабель
        self.input_result = TextInput(text="0", multiline = False) # робимо строку для тексту (типо кнопка)

        lbl_after_res = Label(text="Результат після відпочинку:", halign="right", color=lbl_color, bold=True, font_size=20) # створюємо лабель
        self.input_after_res = TextInput(text="0", multiline = False) # робимо строку для тексту (типо кнопка)


        self.btn = Button(text="Почати", size_hint=(.3, .3), pos_hint={'center_x': .5}, bold=True, background_color=btn_color) # створюємо лабель       
        self.btn.on_press = self.next # кнопка яка буде змінювати екран на другий

        main_line = BoxLayout(orientation="vertical", padding = 10, spacing=15) # мейн лінію робимо
        main_line.add_widget(instr)
        main_line.add_widget(lbl_pulse)
        main_line.add_widget(self.lbl_sec)

        line1 = BoxLayout(size_hint=(.8, None), height="30sp") # лінія для тексту
        line2 = BoxLayout(size_hint=(.8, None), height="30sp") # лінія для тексту

        line1.add_widget(lbl_result)
        line1.add_widget(self.input_result)

        line2.add_widget(lbl_after_res)
        line2.add_widget(self.input_after_res)

        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)

    #def check_sum():


    def next(self): # змінює екран
        global p2, p3
        
        p2 = check_int(self.input_result.text)
        p3 = check_int(self.input_after_res.text)

        if p2 is False or p2 < 1:
            p2 = 0
            self.input_result.text = str(p2)

        elif p3 is False or p3 < 1:
            p3 = 0
            self.input_after_res.text = str(p3)

        else:
            self.manager.current = "fifth"


class ResultScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.instr = Label(text="Ваш індекс Руф'є: -14.8", color=lbl_color, bold=True, font_size=25) # текст
        main_line = BoxLayout(orientation="vertical", size_hint=(.5, .1), pos_hint={'center_x': .5, 'center_y': .5})
        main_line.add_widget(self.instr)


        self.add_widget(main_line)

        self.on_enter = self.result
    
    def result(self):
        self.instr.text = name + "\n" + test(p1, p2, p3, age)

    #def next(self): # змінює екран
        #self.manager.current = "fifth"



class HeartCheck(App): # шоб все працювало
    def build(self):
        sm = ScreenManager()
        sm.add_widget(IntrScr(name = 'first'))
        sm.add_widget(PulseScr(name = 'second'))
        sm.add_widget(SitsScr(name = 'third'))
        sm.add_widget(PulseScr2(name = 'fourth'))
        sm.add_widget(ResultScr(name = 'fifth'))
        return sm
    
app = HeartCheck()
app.run()