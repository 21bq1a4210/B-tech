from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

class Demo(BoxLayout):
    def on_text(self):
        print(self.ti.text)
        print(self.text)
    pass

class Mywdg(BoxLayout,Widget):
    text = Demo.ti.text
    def submit(self):
        #print(self.ti.text)
        print(self.text)
    pass

class MyApp(App):
    pass

if __name__=="__main__":
    MyApp().run()

''''
from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory as F

Builder.load_string("""
<MainScreen>:
    label: label
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Change label text'
            on_press: root.submit(' World')
        Label:
            id: label
            text: 'Hello'

""")


class MainScreen(F.Screen):
    def submit(self, text):
        self.label.text += text

class MainApp(App):
    def build(self):
        return MainScreen()


if __name__ == "__main__":
    MainApp().run()
    '''