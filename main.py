from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout  import AnchorLayout
from kivy.uix.gridlayout  import GridLayout







# class GridLayoutExample(GridLayout):
#     pass
class AnchorLayoutExample(AnchorLayout):
    pass
class BoxLayoutExample(BoxLayout):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = 'vertical'
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3 = Button(text="B")
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)
    pass


class MainWidget(Widget):
    # defines user interface
    pass


class TheLabApp(App):
    pass


TheLabApp().run()
