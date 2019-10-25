#! /usr/bin/python3
import socket                                                     # Import socket module

port = 12345                                                       # Reserve a port for your service.
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # Create a socket object
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()                                            # Getting local machine name                                               
IP = socket.gethostbyname(host)                                        #Getting the server iP
serversocket.bind((host, port))            # Bind to the port
serversocket.listen(1)                     # Now wait for client connection.

print('Server listening....')
print('MY IP is :',IP,'and my PORT is:',port)

while True:
    filename=['first file','second file','third file']
    filename_string = ",".join(filename)
    clientsocket, addr = serversocket.accept()     
    print('Got connection from', addr)
    clientsocket.send(filename_string.encode())
    data = clientsocket.recv(1024)
    data = data.decode()
    print("Client requested : ", data)
    filetomanage = 'sendfile.pdf' #file to be sent
    with open(filetomanage, 'rb') as f:
        packet = f.read(4096)
        while packet:
            clientsocket.send(packet)
            packet = f.read(4096)
    f.close()
    clientsocket.close()
    