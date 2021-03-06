import time
import socket
import select
import sys
import json
from chat_utils import *
# import client_state_machine_m as csm 
import client_state_machine as csm
import threading
import trans
import kivy
from kivy.app import App

class Client:
    def __init__(self, **args):
        # self.console_input = []
        self.peer = ''
        self.state = S_OFFLINE
        self.system_msg = ''
        self.local_msg = ''
        self.peer_msg = ''
        self.usrn = '' # self.name is used in the Kivy library, therefore changed to usrn.
        

    def quit(self):
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()

    def get_name(self):
        return self.usrn

    def init_chat(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
        svr = SERVER # if self.args.d == None else (self.rgs.d, CHAT_PORT)
        self.socket.connect(svr)
        self.sm = csm.ClientSM(self.socket)
        # reading_thread = threading.Thread(target=self.read_input)
        # reading_thread.daemon = True
        # reading_thread.start()

    def shutdown_chat(self):
        return

    def send(self, msg):
        mysend(self.socket, msg)

    def recv(self):
        return myrecv(self.socket)

    def get_msgs(self):
        read, write, error = select.select([self.socket], [], [], 0)
        my_msg = ''
        peer_msg = []
        #peer_code = M_UNDEF    for json data, peer_code is redundant
        if len(trans.trans) > 0:
            my_msg = trans.trans.pop(0)
        if self.socket in read:
            peer_msg = self.recv()
        return my_msg, peer_msg

    def output(self):
        if len(trans.system_msg) > 0:
            trans.local_msg.append(trans.system_msg) # keep track of what's going on
            print(trans.system_msg)
            trans.system_msg = ''

    def send_chat(self):
        if len(trans.system_msg) > 0:
            app = App.get_running_app()
            app.chat(trans.system_msg)
            print(trans.system_msg)
            trans.system_msg = ''

    def login(self):
        my_msg, peer_msg = self.get_msgs()
        if len(my_msg) > 0:
            self.usrn = my_msg
            msg = json.dumps({"action":"login", "name":self.usrn})
            self.send(msg)
            response = json.loads(self.recv())
            if response["status"] == 'ok':
                self.state = S_LOGGEDIN
                self.sm.set_state(S_LOGGEDIN)
                self.sm.set_myname(self.usrn)
                self.print_instructions()
                return (True)
            elif response["status"] == 'duplicate':
                trans.system_msg += 'Duplicate username, try again'
                return False
        else:               # fix: dup is only one of the reasons
           return(False)


    def read_input(self):
        while True:
            text = sys.stdin.readline()[:-1]
            trans.trans.append(text) # no need for lock, append is thread safe

    def print_instructions(self):
        trans.system_msg += menu

    def run_chat(self):
        self.init_chat()
        trans.system_msg += 'Welcome to ICS chat\n'
        trans.system_msg += 'Please enter your name: '
        self.output()
        while self.login() != True:
            self.output()
        trans.system_msg += 'Welcome, ' + self.get_name() + '!'
        self.output()
        while self.sm.get_state() != S_OFFLINE:
            self.proc()
            if self.sm.get_state() == S_LOGGEDIN:
                self.output()
            elif self.sm.get_state() == S_CHATTING:
                self.send_chat()    
            time.sleep(CHAT_WAIT)
        self.quit()

#==============================================================================
# main processing loop
#==============================================================================
    def proc(self):
        my_msg, peer_msg = self.get_msgs()
        trans.system_msg += self.sm.proc(my_msg, peer_msg)
