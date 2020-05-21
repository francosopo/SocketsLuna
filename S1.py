import socket
import threading
import sys
import pickle

class Servidor():
        """docstring for Servidor"""
        def __init__(self, host="localhost", port=8991):

                self.clientes = []
                print(self.clientes)
                self.ident=[]
                print(self.ident)
             
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.bind((str(host), int(port)))
                self.sock.listen(6)
                self.sock.setblocking(False)

                aceptar = threading.Thread(target=self.aceptarconn) #hilo para aceptar
                procesar = threading.Thread(target=self.procesarconn) #hilo para procesar
                
                aceptar.daemon = True
                aceptar.start()
         

                procesar.daemon = True
                procesar.start()
                
      
                
                while True:
                    ident = input('')
                    if ident == 'exit':
                        
                                self.sock.close()
                                sys.exit()
                                print(self.ident)
                    else:
                            pass
                    
                    msg = input('->')
                    if msg == 'salir': 
                        print('Cliente desconectado')
                        self.sock.close()
                        sys.exit()
                    if msg== ':smile':
                        print(':-)')
                    if msg == ':angry':
                        print ('>:(')
                    if msg == ':confused':
                        
                        print(':S')
                    else:
                        continue
                    
    
                                    
    
             
        def msg_to_all(self, msg, cliente):
            	for c in self.clientes:
                    try:
                        if c != cliente:
                            c.send(msg)
                    except:
                        self.clientes.close()                         


        def aceptarconn(self):
                print("Aceptar iniciado")
                while True:
                    try:
                        conn, addr = self.sock.accept()
                        conn.setblocking(False)
                        cliente = Cliente(conn,0,conn.getsockname())
                        self.clientes.append(cliente)
                    except: 
                        pass
                       

        def procesarconn(self):
            print("Procesar iniciado")
            while True:
                if len(self.clientes) > 0:
                    for c in self.clientes:
                        try:
                            data = c.recv(1024)
                            c.increaseMsg()
                            if data and c.getContador() != 1:
                                print(data)
                                self.msg_to_all(data,c)
                        except:
                            pass
               
 

        def mostrar(self):
            print(self.clientes,"and",self.ident)

class Cliente:
    def __init__(self, conn,contMsg, ip):
        self.__cliente = conn
        self.__contMsg = contMsg
        self.__ip = ip

    def getCliente(self):
        return self.__cliente
    def getContador(self):
        return self.__contMsg
    def recv(self,num):
        return self.__cliente.recv(num)
    def send(self,msg):
        return self.__cliente.send(msg)
    def increaseMsg(self):
        self.__contMsg +=1
    def getSockName(self):
        return self.__ip
s = Servidor()

