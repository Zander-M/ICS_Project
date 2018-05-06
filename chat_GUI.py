import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
import threading
import trans

# from kivy.uix.dropdown import DropDown
# test login
# Builder.load_file("kv\\command.kv") # test command
# Builder.load_file("kv\\sonnet.kv") # test sonnet
# Builder.load_file("kv\\chatting.kv")

class login(Screen):
   
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.ids['usrn'].bind(on_text_validate=self.usrlgin)

    def usrlgin(self, *args):
        app = App.get_running_app()
        app.usrn = self.ids['usrn'].text
        app.cmd(app.usrn)
        while trans.system_msg == '':
            pass
        if trans.system_msg[0] == 'D':
            app.popup('Oops, duplicated name. Try another?')
        else:
            app.scrm.current = 'command'
            app.popup('Welcome! ' + app.usrn + '!')

class notice(Popup):
    pass

class command(Screen):
    
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
    # logged in stage panel.
    
    # def on_enter(self, *args):
    #     app = App.get_running_app()
    #     self.ids['cmd_usrn'].text = "Hello, " + app.usrn + '\nWhat do you want to do?' # change the username on the command panel

    def bye(self):
        # log out of the system
        app = App.get_running_app()
        trans.trans.append('q')
        app.stop()

class chat_with(Screen):
    pass

class chatting(Screen):
    # chatting stage panel
    pass

class sonnet(Screen):
    # sonnet stage panel
    pass
    


class mainCanvas(Widget):
    # this is the main canvas handling tasks
    pass
    # return commandPanel() 

class Chat_GUI(App):

    def __init__(self):
        super().__init__()
        self.usrn = '' # variable that stores the username
        self.notice = '' # content of the popup window

    def build(self):
        Builder.load_file("kv\\chat_system.kv") # load layout files 
        self.scrm = ScreenManager()
        self.scrm.add_widget(login(name='login'))
        self.scrm.add_widget(command(name='command', id='command'))
        self.scrm.add_widget(chat_with(name='chat_with'))
        self.scrm.add_widget(chatting(name='chatting'))
        self.scrm.add_widget(sonnet(name='sonnet'))
        return self.scrm
    
    def cmd(self, text):
        trans.trans.append(text)
        
    def popup(self, msg):
        # popup window. pass in message to pop up. click ok to close.
        p = notice()
        p.ids['msg'].text = msg
        p.open()
        self.notice = ''
    
    # chatThread.start()    
    # def update(self, screen):
    #     if screen == 0:
    #         sm.current('')        
    #     elif screen == 1:
    #         sm.current('')
    #     elif screen == 2:
    #         sm.current('')
    #     else:
    #         pass

def main():
    a = Chat_GUI()
    a.run()

if __name__ == '__main__':
    main()