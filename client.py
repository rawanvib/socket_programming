import socket

client = socket.socket()

# server will bind socket to to port number
client.connect(('localhost',9999))

name=input("Ener your name: ")

client.send(bytes(name,'utf-8'))

print(client.recv(1024).decode())

