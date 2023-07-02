from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

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
        txt = Label(text = "екран1")
        self.add_widget(txt) 

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt = Label(text = "екран2")
        self.add_widget(txt)

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