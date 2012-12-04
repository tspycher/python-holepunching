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
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.bind(('',5555))
        sock.sendto("blubb", (self.serverIP, self.serverPort))
        
        print "listening on %s" % (sock.getsockname(),)
        
        received = False
        
        while not received:
            message = sock.recv(10240)
            print "received message: %s" % message
            if message:
                received = True
                if message.startswith(":"):
                    data = message[1:].split(",")
                    clientIP = data[0]
                    clientPort = data[1]
                    print "client: %s:%s" % (clientIP, clientPort)
                    sock.sendto("hello client", (clientIP, int(clientPort)))     
        
if __name__ == "__main__":
    #client = Client("cloud01.sourcetube.net", 5555)
    client = Client("10.84.1.116", 5555)
    client.start()