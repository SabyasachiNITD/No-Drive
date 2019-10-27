#! /usr/bin/python3
import socket
def create_server():
    port = 12345                                                      
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = socket.gethostname()                                                                                        
    IP = socket.gethostbyname(host)                                        
    serversocket.bind((host, port))            
    serversocket.listen(1)                     

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
        