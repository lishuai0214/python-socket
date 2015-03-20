#!/bin/python
#python version 3.1+
import socket
import threading

class ConnectHandler(threading.Thread):
    def setConnect(self, connect):
        self.connect = connect
    
    def run(self): 
        msg = 'hello'.encode("utf-8")               
        self.connect.send(msg)
        self.connect.close()
        
class TestServer:    
    def __init__(self, ip='0.0.0.0', iPort=8771):    
        
        self.ip = ip
        self.iPort = iPort
    
    def start(self):        
        print("TestServer start({0}:{1})...".format(self.ip, self.iPort))
                
        cc = 1        
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ss.settimeout(1000 * 10)
        ss.bind((self.ip, self.iPort))
        ss.listen(5)
        
        while cc <= 5: 
#        while True:
            (client, address) = ss.accept()
            print("client connecting:",cc)
            cc+=1            
            ch = ConnectHandler()
            ch.setConnect(client)
            ch.start()
            #client.send(b'hello')
            #client.close()
        ss.close()
        print("TestServer close, bye-bye.")    
    
    
if __name__ == "__main__":
    ts = TestServer()
    ts.start()
