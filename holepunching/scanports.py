'''
Created on 04.12.2012

@author: pescado
'''
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

for port in range(30000, 40000):
    sock.sendto("blubb", ("10.10.20.1", port))
    print "scan port %s", port