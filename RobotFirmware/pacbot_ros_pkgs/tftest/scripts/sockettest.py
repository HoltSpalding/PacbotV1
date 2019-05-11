import socket
import sys
import struct

address = ('130.64.160.136', 11297)
client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
z = client_socket.connect_ex(address)
print(z)
print("connection successful")
while True:
    print("listening")
    totallen = client_socket.recv(4)
    print(totallen)
    totallenRecv = struct.unpack('>I', totallen)[0]
    message = client_socket.recv(totallenRecv)
    print(message)
