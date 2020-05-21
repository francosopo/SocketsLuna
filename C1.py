import socket
import threading
import sys
import pickle

class Cliente():
        """docstring for Cliente"""
        def __init__(self, host="localhost", port=8991):

                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((str(host), int(port)))

                msg_recv = threading.Thread(target=self.msg_recv)

                msg_recv.daemon = True
                msg_recv.start()
                ident=input('[CLIENT]: Identificacion> ')
                print("\n")
                if ident != 'error':
                        self.send_ident(ident)
                else:
                        self.sock.close()
                        sys.exit()
                        self.sock.send(ident.encode('utf-8'))
                while True:
                        #ident=input('Ingresa tu nick:')
                        msg = input('->')
                        if msg != 'salir':                                
                                self.send_msg(msg)
                        else:
                                print('se desconecto')
                                self.sock.close()
                                sys.exit()

        def msg_recv(self):
                while True:
                        try:
                                data = self.sock.recv(1024)
                                if data:
                                        print(pickle.loads(data))
                        except:
                                pass

        def send_msg(self, msg):
                self.sock.send(pickle.dumps(msg))


        def send_ident(self,ident):
                self.sock.send(pickle.dumps(ident))


c = Cliente()
                
