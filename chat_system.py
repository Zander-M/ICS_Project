# import subprocess
# import sys, time
from chat_GUI import *
import threading
from chat_client_class import *
import trans


def commute(text):
    global trans
    trans = text

class ChatSystem:
    
    def __init__(self):
        self.c_sys = Client()
        self.g_sys = Chat_GUI()
        self.trdlock = threading.Lock()
    
    def build(self):
        Builder.load_file("kv\\chat_system.kv") # load layout files 
        self.scrm = ScreenManager()
        self.scrm.add_widget(login(name='login'))
        self.scrm.add_widget(command(name='command'))
        self.scrm.add_widget(chat_with(name='chat_with'))
        self.scrm.add_widget(chatting(name='chatting'))
        self.scrm.add_widget(sonnet(name='sonnet'))
        return self.scrm

    # def init_chat(self):
    #     self.c_sys.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    #     svr = SERVER # if self.args.d == None else (self.rgs.d, CHAT_PORT)
    #     self.c_sys.socket.connect(svr)
    #     self.c_sys.sm = csm.ClientSM(self.socket)
    #     # reading_thread = threading.Thread(target=self.g_sys.cmd('zd','login'))
    #     # reading_thread.daemon = True
    #     # reading_thread.start()
    

    def run_app(self):
        self.g_sys.run()

    def run_C_sys(self):
        self.c_sys.run_chat()
            # self.c_sys.console_input.append(self.trans)
            # self.trans = ''
        # while self.trans != '':
        #     self.c_sys.console_input.append(self.trans)
        #     self.trans = ''

    def tst(self):
        while len(trans.trans) != 0:
            self.c_sys.console_input.append(trans.trans)
            trans.trans = [] 

    def trdctrl(self): # starting two threads, chat system and GUI
        # self.c_sys.run_chat()
        # self.g_sys.run(
        chatThread = threading.Thread(target=self.run_C_sys)
        appThread = threading.Thread(target=self.run_app)
        testThread = threading.Thread(target=commute, args=['test'])
        appThread.start()
        chatThread.start()
        testThread.start()
        testThread.join()
        appThread.join()
        chatThread.join()
 
if __name__ == '__main__':
    chat = ChatSystem()
    chat.trdctrl()

# Testing code
# from chat_client_class import *
# import threading
# import kivy
# from kivy.uix.button import Button
# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.label import Label
# from kivy.uix.scrollview import ScrollView
# from kivy.uix.gridlayout import GridLayout
# from kivy.event import EventDispatcher

# # kv = Builder.load_string('''
# # <Test>
# #     GridLayout:
# #         cols:1
# #         size: root.size
# #         Button:
# #             text: 'hello'
# #             on_press: root.a()

# # ''')

# class Test(Button):
#     def a(self):
#         app = App.get_running_app()
#         app.cmd('zd')

# class ChatSys(App, Client):
#     def __init__(self):
#         super().__init__()
#         self.msg = ''
    
#     def build(self):
#         return Test()


#     def init_chat(self):
#         self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
#         svr = SERVER # if self.args.d == None else (self.rgs.d, CHAT_PORT)
#         self.socket.connect(svr)
#         self.sm = csm.ClientSM(self.socket)
#         reading_thread = threading.Thread(target=self.test)
#         reading_thread.daemon = True
#         reading_thread.start()

#     def cmd(self, text):
#         self.console_input.append(text)
#         return

#     def test1(self):
#         # login_GUI.ChatSystem().run()
#         chatThread = threading.Thread(target=self.run_chat())
#         guiThread = threading.Thread(target=self.run())  
#         # chatThread.daemon = True
#         guiThread.start()
#         chatThread.start()
                
#     def test(self):
#         self.run()
# def run_client():
#     client = chat_client_class.Client()
#     client.run_chat()
#     cliserver = subprocess.Popen(client.run_chat(), stdout=subprocess.PIPE, stdin=subprocess.PIPE)

# def run_GUI():
#     login_GUI.GUI()

# def test():
    
# t1 = threading.Thread(target=test)
# t2 = threading.Thread(target=run_client)
# run_client()
    # t2.start()
    # t1.start()