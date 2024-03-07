from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout  import AnchorLayout
from kivy.uix.gridlayout  import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
class WidgetsExample(GridLayout):
    my_text = StringProperty("Hello!")
    count = 1
    # state = StringProperty("OFF")
    count_enabled = BooleanProperty(False)
    #slider_value_txt = StringProperty('Value')


    def on_button_click(self):
        #if self.state == 'ON':
        if self.count_enabled == True:
            print('Button Clicked')
            print(self.count)
            self.count = self.count + 1
            self.my_text = str(self.count)


    def on_toggle_button_state(self,toggle_button):
        print('Toggle State' + toggle_button.state )
        if toggle_button.state == 'normal':
            # self.state ='OFF'
            toggle_button.text = 'off'
            self.count_enabled = False
        else:
         # self.state='ON'
             toggle_button.text = 'on'
             self.count_enabled = True

    def on_switch_active(self,widget):
        print('Switch active' + str(widget.active))

    def on_slider_value(self, widget):
        print('Slider' + str(int(widget.value)))
        #self.slider_value_txt =str(int(widget.value))










    pass



class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'lr-tb'
        for i in range(0,100):
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None,None), size =(size,size))
            self.add_widget(b)


    pass
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
