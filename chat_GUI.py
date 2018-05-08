import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
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
        if self.ids['usrn'].text.strip() == '':
            app.popup('Username cannot be empty!')

        else:
            app.usrn = self.ids['usrn'].text.strip()
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

class selfmsg(Label):
    pass

class peermsg(Label):
    pass

class command(Screen):
    
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
           # logged in stage panel.
    
    def showUsr(self):
        app = App.get_running_app()
        app.showUsr()
    # def on_enter(self, *args):
    #     app = App.get_running_app()
    #     self.ids['cmd_usrn'].text = "Hello, " + app.usrn + '\nWhat do you want to do?' # change the username on the command panel

    def bye(self):
        # log out of the system
        app = App.get_running_app()
        trans.trans.append('q')
        app.stop()

class chat_with(Popup):
    
    def __init__(self, **kwargs):
        super().__init__()
        self.app = App.get_running_app()
    
    def show_usrls(self):
        self.app.getusrls()
        while self.app.usrls == []:
            pass
        self.ids['usrls'].clear_widgets()
        if len(self.app.usrls) > 1 : # update the dropdown list 
            for i in self.app.usrls.keys():
                if i != self.app.usrn:
                    btn = Button(text=i, size_hint_y=None, height=60)
                    btn.bind(on_release=lambda btn: self.ids['usrls'].select(btn.text))
                    self.ids['usrls'].add_widget(btn)
                else:
                    pass
            self.ids['usrls'].open(self.ids['slt_usr'])
        # if len(app.usrls) != 0: 
        #     for i in app.usrls:
        #         self.ids['usr_ls'].add_widget(Button(text=i, on_release=parent.select(i)))
        else:
            self.app.popup('Oops, no available user!')
    
    def connect(self):
        self.app.cmd('c'+ self.ids['slt_usr'].text)
        while trans.system_msg == '':
            pass
        self.dismiss()
        # if trans.system_msg[0] == 'Y':
        #     app.scrm.current = 'chatting'
        # else:
        #     app.popup('Oops, something went wrong...')
        
    def reset(self):
        self.ids['slt_usr'].text = 'who?'

class chatting(Screen):

    def __init__(self, **kwargs):
        super(chatting, self).__init__(**kwargs)
        self.trdlock = threading.Lock()
        # self.listen = threading.Thread(target=self.listen())
        # self.listen.start()
        # self.listen.join()

    def send(self):
        app = App.get_running_app()
        if self.ids['msg'].text == '':
            app.popup("Can't send empty message!")
            return
        else:
            app.cmd(self.ids['msg'].text)
            self.ids['display'].text += '['+ app.usrn + ']:\n' + self.ids['msg'].text + '\n\n'
            self.ids['msg'].text = ''
            return
    
    # def listen(self):
    #     while trans.system_msg != '':
    #         self.trdlock.acquire()
    #         self.ids['display'].text += trans.system_msg
    #         if trans.system_msg == 'bye':
    #             break
    #         self.trdlock.release()
        return
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
        self.usrls = [] # current usr in dict
        # self.listen = threading.Thread(target=self.listen)
        # self.listen.start()
        # self.listen.join()
        # self.trdlock = threading.Lock()

    def build(self):
        Builder.load_file("kv\\chat_system.kv") # load layout files 
        self.scrm = ScreenManager()
        self.scrm.add_widget(login(name='login'))
        self.scrm.add_widget(command(name='command', id='command'))
        # self.scrm.add_widget(chat_with(name='chat_with'))
        self.scrm.add_widget(chatting(name='chatting'))
        self.scrm.add_widget(sonnet(name='sonnet'))
        return self.scrm

    def cmd(self, text):
        trans.trans.append(text)
    
    def rtcmd(self):
        self.scrm.current = 'command'
    
    def getusrls(self):
        trans.trans.append('who')
        while trans.system_msg == '':
            pass
        import ast
        self.usrls = ast.literal_eval(trans.system_msg)
        return 
    
    def showUsr(self):
        p = chat_with()
        p.open()

    def chat(self, text):   
        self.scrm.screens[2].ids['display'].text += text + '\n' # adding peer msg
        pass

    def popup(self, msg):
        # popup window. pass in message to pop up. click ok to close.
        p = notice()
        p.ids['msg'].text = msg
        p.open()
        self.notice = ''
    
    # def listen(self):
    #     while self.scrm.current == 'command' and trans.system_msg[0] == 'R':
    #         self.trdlock.acquire()
    #         self.popup('Request from: {}'.format(trans.system_msg[13: trans.system_msg.find('/')]))
    #         self.scrm.current = 'chatting'
    #         self.trdlock.release()

    
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