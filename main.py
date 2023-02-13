from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.8, 0.8)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        #add widgets to window

        self.window.add_widget(Image(source="images/logo.png"))

        self.greeting = Label(text="Hello World",
                              font_size=32,
                              color = "#00FF00"
                              )
        self.window.add_widget(self.greeting)

        self.user = TextInput(multiline=False,
                              padding_y=(20, 20),
                              size_hint=(1, 0.5),
                              padding_x=(20, 20)
                              )
        self.window.add_widget(self.user)

        self.button = Button(text="Click Me",
                             size_hint=(1, 0.5),
                             bold=True,
                             background_color="#00FF00"

                             )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        self.greeting.text = f"Hello {self.user.text}"



if __name__ == "__main__":
    SayHello().run()
