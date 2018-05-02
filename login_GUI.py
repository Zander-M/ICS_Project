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
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file("kv\\chat_system.kv") # test login
# Builder.load_file("kv\\command.kv") # test command
# Builder.load_file("kv\\sonnet.kv") # test sonnet
# Builder.load_file("kv\\chatting.kv")
class loginIcon(Widget):
    pass

class login(Screen):
    # log in stage panel
    pass

class command(Screen):
    # logged in stage panel
    pass

class chatting(Screen):
    # chatting stage panel
    pass

class sonnet(Screen):
    # sonnet stage panel
    pass
    
sm = ScreenManager()
sm.add_widget(login(name='login'))
sm.add_widget(command(name='command'))
sm.add_widget(chatting(name='chatting'))
sm.add_widget(sonnet(name='sonnet'))

class mainCanvas(Widget):
    # this is the main canvas handling tasks
    pass
    # return commandPanel() # test command panel
    # test login panel
    # return chattingPanel() # test chatting panel

class ChatSystem(App):

    def build(self):
        return sm
    
    def popup(self):
        pass
    
    def update(self, screen):
        if screen == 0:
            sm.current('')        
        elif screen == 1:
            sm.current('')
        elif screen == 2:
            sm.current('')
        else:
            pass



if __name__ == '__main__':
    ChatSystem().run()