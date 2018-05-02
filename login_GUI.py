import kivy

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder

# Builder.load_file("kv\\login.kv") # test login
# Builder.load_file("kv\\command.kv") # test command
Builder.load_file("kv\\sonnet.kv") # test sonnet
class loginIcon(Widget):
    pass

class loginPanel(GridLayout):
    # log in stage panel
    pass

class commandPanel(GridLayout):
    # logged in stage panel
    pass

class chattingPanel(GridLayout):
    # chatting stage panel
    def __init__(self, **kwarg):
        super(chattingPanel, self).__init__(**kwarg)
        pass

class mainCanvas(Widget):
    # this is the main canvas handling tasks
    pass
    # return commandPanel() # test command panel
    # test login panel
    # return chattingPanel() # test chatting panel

class ChatSystem(App):

    def build(self):
        return mainCanvas()
    
    def update(self, screen):
        pass



if __name__ == '__main__':
    ChatSystem().run()