from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class MyGrid(BoxLayout):
    first_name_input = ObjectProperty()
    second_name_input = ObjectProperty()
    email_input = ObjectProperty()
    fist_name,second_name,email = StringProperty(''), StringProperty(''), StringProperty('')
    def pressed(self,wdg):
        print("Button clicked")
        self.fist_name=self.first_name_input.text
        self.second_name = self.second_name_input.text
        self.email = self.email_input.text
        print(self.fist_name, self.second_name, self.email)

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MyApp(App):
    pass

if __name__=="__main__":
    MyApp().run()