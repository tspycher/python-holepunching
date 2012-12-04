'''
Created on Dec 4, 2012

@author: thospy
'''
import socket

class Client(object):
    
    serverIP = None
    serverPort = None
    
    def __init__(self, serverIp, serverPort):
        self.serverIP = serverIp
        self.serverPort = serverPort
        
    def start(self):
        sockToServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sockToServer.sendto("hello", (self.serverIP, self.serverPort))
        
        received = False
        
        while not received:
            message = sockToServer.recv(10240)
            if message:
                received = True
                if message.startswith(":"):
                    data = message[1:].split(",")
                    clientIP = data[0]
                    clientPort = data[1]
        
        sockToServer.sendto("hello client", (clientIP, clientPort))     
        
if __name__ == "__main__":
    client = Client("10.84.1.116", 5555)
    client.start()