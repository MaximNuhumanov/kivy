from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class ScrButton(Button):
    def __init__(self, screen, direction = 'right', goal = 'main', **kwargs):
        super().__init__(**kwargs)
        self.screen =screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal



class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        hBox = BoxLayout()
        vBox = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)

        txt = Label(text = "Oбери екран")

        button1 = ScrButton(self, direction='down', goal='first', text = "1")
        button2 = ScrButton(self, direction='left', goal='second', text = "2")
        button3 = ScrButton(self, direction='up', goal='third', text = "3")
        button4 = ScrButton(self, direction='right', goal='fourth', text = "4")

        vBox.add_widget(button1)
        vBox.add_widget(button2)
        vBox.add_widget(button3)
        vBox.add_widget(button4)

        hBox.add_widget(txt)
        hBox.add_widget(vBox)
        self.add_widget(hBox)               
        
class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        v1box = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8, size_hint = (0.5, 0.5), pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        btn = Button(text = "Вибір 1", size_hint = (0.5, 1), pos_hint = {'left': 0})
        return_btn = ScrButton(self, direction='up', goal='main', text = "back", size_hint = (0.5, 1), pos_hint = {'right': 1})
        v1box.add_widget(btn)
        v1box.add_widget(return_btn)
        self.add_widget(v1box)                                                                      


class SecondScreen(Screen):                            
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.txt = Label(text = "екран2")
        txt2 = Label(text = "Введіть пароль:")
        self.inpt = TextInput(multiline = False)
        v2box = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        h2box = BoxLayout( size_hint =(0.8, None), height = '30sp')
        h3box = BoxLayout(size_hint =(0.5, 0.2), pos_hint={'center_x':0.5})
        h2box.add_widget(txt2)
        h2box.add_widget(self.inpt)
        
        return2_btn = ScrButton(self, direction='right', goal='main', text = "Back")
        btn_ok = Button(text = "OK")
        btn_ok.on_press = self.change_text
        v2box.add_widget(self.txt)
        v2box.add_widget(h2box)
        h3box.add_widget(btn_ok)
        h3box.add_widget(return2_btn)
        v2box.add_widget(h3box)
        
        self.add_widget(v2box)
        
    def change_text(self):
        self.txt.text = self.inpt.text + " Не подходит"
        
class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt = Label(text = "екран3")
        self.add_widget(txt)

class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt = Label(text = "екран4")
        self.add_widget(txt)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name = 'main'))
        sm.add_widget(FirstScreen(name ='first'))
        sm.add_widget(SecondScreen(name ='second'))
        sm.add_widget(ThirdScreen(name ='third'))
        sm.add_widget(FourthScreen(name ='fourth'))
        return sm
        

app = MyApp()
app.run()