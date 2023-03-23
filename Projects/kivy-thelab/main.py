import kivy
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout


class WidgetExample(GridLayout):
    my_text = StringProperty("HELLO")
    ButtonCount = 0

    def onButtonClick(self):
        self.ButtonCount += 1
        self.my_text = f"{self.ButtonCount}"
        # print("Button clicked")


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        for i in range(1, 101):
            dsize = dp(100)
            b = Button(
                text=f"{i}",
                size_hint=(None, None),
                size=(dsize, dsize)
            )
            self.add_widget(b)


class AnchorLayoutExample(AnchorLayout):
    pass


'''
class GridLayoutExample(GridLayout):
    pass
'''


class BoxLayoutExample(BoxLayout):
    '''def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
    '''


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


if __name__ == "__main__":
    TheLabApp().run()
