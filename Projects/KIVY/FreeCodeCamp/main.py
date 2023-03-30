import kivy
from kivy.app import App
from kivy.graphics import Line, Color, Rectangle
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout


class WidgetExample(GridLayout):
    my_text = StringProperty("HELLO")
    ButtonCount = 0
    count_enabled= BooleanProperty(False)
    #slide_val=StringProperty("slider value")
    text_input_str=StringProperty("Foo")
    def onButtonClick(self):
        if self.count_enabled==True:
            self.ButtonCount += 1
            self.my_text = f"{self.ButtonCount}"
        # print("Button clicked")
    def onToggleButtonState(self,widget):
        #print("Toggle button clicked")
        if widget.state=="normal":
            widget.text="OFF"
            self.count_enabled=False
        else:
            widget.text="ON"
            self.count_enabled=True
    def onActive(self,widget):
        print(f"{widget.active}")

    def onSliderValue(self,widget):
        #print(f"Slider:{widget.value}")
        #self.slide_val=f"{int(widget.value)}"
        pass
    def onTextvalidate(self,widget):
        self.text_input_str=widget.text
        pass

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100,100,400,500), width=2)
            Color(0,1,0)
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(700, 500, 150, 100), width=2)
            self.rect=Rectangle(pos=(700, 200), size=(150,100))
    def on_click(self):
        #print("foo")
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)
        diff = self.width - (x+w)

        if diff < inc:
            inc = diff
        x += inc
        self.rect.pos = (100, 100)
        self.rect.pos = (x, y)
        pass

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