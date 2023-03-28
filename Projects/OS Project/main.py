from kivy.app import App
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget

class MainWindow(Screen):
    pass


class Tabel(BoxLayout):
    def values(self,obj):
        print(obj)
    pass

class FCFS(Screen):
    def clicked_fcfs(self,wdg):
        print(1)
        pass
    def submit(self,wdg):
        print(2)
        pass

class SJF(Screen):
    pass

class RR(Screen):
    pass

class Priority(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class OsTimeSchdulingAlgoApp(App):
    pass

if __name__=="__main__":
    OsTimeSchdulingAlgoApp().run()