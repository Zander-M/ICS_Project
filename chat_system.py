# import subprocess
# import sys, time
from chat_GUI import *
import threading
from chat_client_class import *
import trans

trans.trans = []
trans.local_msg = []
trans.system_msg = ''

class ChatSystem:
    
    def __init__(self):
        self.c_sys = Client()
        self.g_sys = Chat_GUI()
        self.trdlock = threading.Lock()
    
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

    # def tst(self):
    #     while len(trans.trans) != 0:
    #         self.c_sys.console_input.append(trans.trans)
    #         trans.trans = [] 

    def trdctrl(self): # starting two threads, chat system and GUI
        # self.c_sys.run_chat()
        # self.g_sys.run(
        chatThread = threading.Thread(target=self.run_C_sys)
        appThread = threading.Thread(target=self.run_app)
        # testThread = threading.Thread(target=commute, args=['test'])
        appThread.start()
        chatThread.start()
        # testThread.start()
        # testThread.join()
        appThread.join()
        chatThread.join()

 
if __name__ == '__main__':
    chat = ChatSystem()
    chat.trdctrl()
