'''
Created on Dec 4, 2012

@author: thospy
'''
from SocketServer import UDPServer, BaseRequestHandler #,ThreadingMixIn,ThreadingUDPServer,ForkingUDPServer
import base64
import os
import threading
import time


class _PunchingServer(UDPServer):
    daemon_threads = False

class Server(BaseRequestHandler):
    '''
    classdocs
    '''
    
    _remotesPool = []

    def setup(self):
        pass
        
    def handle(self):        
        print "message: %s from %s " %  (self.request[0], self.client_address)
        socket = self.request[1]
        self.addRemotes(socket)
        print socket
        socket.sendto("Thank you", self.client_address)
    
    def addRemotes(self, socket):
        if len(self._remotesPool) < 2:
            print "having less than 2 connections"
            self._remotesPool.append(socket)
        else:
            print "having two Clients"
            print self._remotesPool
            
    @staticmethod
    def startServer(ip = "", port = 5555):
        addr = (ip, port)
        
        print "listening on %s:%s" % addr
        server = _PunchingServer(addr, Server)
        th = threading.Thread(target=server.serve_forever)
        th.start()
       
if __name__ == "__main__":
    Server.startServer()