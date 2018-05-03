# import subprocess
# import sys, time
# import login_GUI
from chat_client_class import *
import threading
import kivy
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder

kv = Builder.load_string('''
<Test>:
    Button:
        text: 'hello'
        on_press: app.testprint()
''')

class Test(Button):
    pass

class ChatSys(App, Client):
    def __init__(self):
        super().__init__()
        self.msg = ''
    
    def build(self):
        return Test()

    def init_chat(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
        svr = SERVER # if self.args.d == None else (self.rgs.d, CHAT_PORT)
        self.socket.connect(svr)
        self.sm = csm.ClientSM(self.socket)
        reading_thread = threading.Thread(target=self.test)
        reading_thread.daemon = True
        reading_thread.start()

    def testprint(self):
        self.console_input.append('zd')
        return

    def test1(self):
        # login_GUI.ChatSystem().run()
        chatThread = threading.Thread(target=self.run_chat())
        guiThread = threading.Thread(target=self.test())  
        # chatThread.daemon = True
        guiThread.start()
        chatThread.start()
                
    def test(self):
        self.run()
# def run_client():
#     client = chat_client_class.Client()
#     client.run_chat()
#     cliserver = subprocess.Popen(client.run_chat(), stdout=subprocess.PIPE, stdin=subprocess.PIPE)

# def run_GUI():
#     login_GUI.GUI()

# def test():
    
# t1 = threading.Thread(target=test)
# t2 = threading.Thread(target=run_client)

if __name__ == '__main__':
    chat = ChatSys()
    chat.test1()  # run_client()
    # t2.start()
    # t1.start()