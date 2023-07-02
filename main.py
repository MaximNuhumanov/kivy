from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        hBox = BoxLayout()
        vBox = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)

        txt = Label(text = "Oбери екран")

        button1 = Button(text = "1")
        button2 = Button(text = "2")
        button3 = Button(text = "3")
        button4 = Button(text = "4")

        vBox.add_widget(button1)
        vBox.add_widget(button2)
        vBox.add_widget(button3)
        vBox.add_widget(button4)

        hBox.add_widget(txt)
        hBox.add_widget(vBox)
        self.add_widget(hBox)               
        







class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name = 'main'))
        return sm
        

app = MyApp()
app.run()