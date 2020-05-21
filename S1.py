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
                                continue
                    
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
                        self.clientes.append(conn)
                    except: 
                            pass
                       

        def procesarconn(self):
                print("Procesar iniciado")
                while True:
                        if len(self.clientes) > 0:
                                for c in self.clientes:
                                        try:
                                                
                                                data = c.recv(1024)
                                                if data:
                                                        print(data)
                                                        self.msg_to_all(data,c)
                                        except:
                                                pass
               
 

        def mostrar(self):
            print(self.clientes,"and",self.ident)
        
s = Servidor()

