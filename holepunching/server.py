'''
Created on Dec 4, 2012

@author: thospy
'''
from SocketServer import UDPServer, BaseRequestHandler #,ThreadingMixIn,ThreadingUDPServer,ForkingUDPServer
import socket

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
        #socket = self.request[1]
        self.addRemotes(self.request[0], self.client_address)
        #if backval:
            #socket.sendto(backval, self.client_address)
    
    def addRemotes(self, identifier, address):
        if not identifier in self._remotesPool:
            self._remotesPool[identifier] = []
            
        #self._remotesPool[identifier].append([address[0], address[1], socket])
        self._remotesPool[identifier].append(address)

        #self._remotesPool[identifier].append(socket)

        print self._remotesPool
        
        if len(self._remotesPool[identifier]) < 2:
            print "having still less than 2 connections"
            return None
        
        print "having two Clients"
        #self._remotesPool = []
        #print self._remotesPool
        connectionStringA = ":%s,%i" % (self._remotesPool[identifier][0][0], self._remotesPool[identifier][0][1])
        connectionStringB = ":%s,%i" % (self._remotesPool[identifier][1][0], self._remotesPool[identifier][1][1])
        #socketA = self._remotesPool[identifier][0][2]
        #socketB = self._remotesPool[identifier][1][2]
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

        sock.sendto(connectionStringB,self._remotesPool[identifier][0])
        sock.sendto(connectionStringA,self._remotesPool[identifier][1])

        self._remotesPool.pop(identifier)
        #return connectionString
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