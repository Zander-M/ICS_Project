import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
# from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import threading
from chat_system import commute
import trans
# from kivy.uix.dropdown import DropDown

# test login
# Builder.load_file("kv\\command.kv") # test command
# Builder.load_file("kv\\sonnet.kv") # test sonnet
# Builder.load_file("kv\\chatting.kv")
class login(Screen):
   
    def usrlgin(self):
        app = App.get_running_app()
        app.usrn = self.ids['usrn'].text
        app.cmd('zd', 'command')

class notice(Popup):
    pass

class command(Screen):
    # logged in stage pane
    def bye(self):
           trans.trans.append('q')
           App.get_running_app().stop()

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
    # return commandPanel() # test command panel
    # test login panel
    # return chattingPanel() # test chatting panel
       
class Chat_GUI(App):

    def __init__(self):
        super().__init__()
        self.usrn = ''
        self.lk = threading.Lock()

    def build(self):
        Builder.load_file("kv\\chat_system.kv") # load layout files 
        self.scrm = ScreenManager()
        self.scrm.add_widget(login(name='login'))
        self.scrm.add_widget(command(name='command'))
        self.scrm.add_widget(chat_with(name='chat_with'))
        self.scrm.add_widget(chatting(name='chatting'))
        self.scrm.add_widget(sonnet(name='sonnet'))
        return self.scrm
    
    def cmd(self, text, scn):
        trans.trans.append(text)
        while trans.system_msg == '':
            pass
        if trans.local_msg[-1][0]=='D':
            self.popup(self.scrm.current)
        else:
            self.scrm.current = 'command'
        
    def popup(self, scn):
        p = notice()
        p.open()
    
   
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