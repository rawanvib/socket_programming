import socket

# create server socket
server=socket.socket()
print("Socket created")

# bind socket to port
server.bind(('localhost',9999))

# listen to client
server.listen()
print("Waiting for connection")

while True:
    client_port,address=server.accept()

    name=client_port.recv(1024).decode()

    print(("Connected with {} having address {}").format(name,address))
    client_port.send(bytes('Message from server','utf-8'))

    client_port.close()