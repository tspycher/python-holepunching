'''
Created on Dec 4, 2012

@author: thospy
'''
from SocketServer import UDPServer, BaseRequestHandler #,ThreadingMixIn,ThreadingUDPServer,ForkingUDPServer
import base64
import os
import threading
import time
import pickle


class _PunchingServer(UDPServer):
    daemon_threads = False

class Server(BaseRequestHandler):
    '''
    classdocs
    '''
    
    _remotesPool = {}

    def setup(self):
        pass
        
    def handle(self):        
        print "message: %s from %s " %  (self.request[0], self.client_address)
        socket = self.request[1]
        backval = self.addRemotes(self.client_address)
        if backval:
            socket.sendto(backval, self.client_address)
    
    def addRemotes(self, identifier, address):
        if not identifier in self._remotesPool:
            self._remotesPool[identifier] = []
            
        self._remotesPool[identifier].append(address)
        
        print self._remotesPool
        
        if len(self._remotesPool) < 2:
            print "having still less than 2 connections"
            return None
        
        print "having two Clients"
        #self._remotesPool = []
        #print self._remotesPool
        return ":%s,%i" % (self._remotesPool[identifier][0][0], self._remotesPool[identifier][0][1])
        #print self._remotesPool
            
    @staticmethod
    def startServer(ip = "", port = 5555):
        addr = (ip, port)
        
        print "listening on %s:%s" % addr
        server = _PunchingServer(addr, Server)
        th = threading.Thread(target=server.serve_forever)
        th.start()
       
if __name__ == "__main__":
    Server.startServer()