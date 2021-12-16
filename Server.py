import socket
# socket.AF_INET represents the IPv4 , and socket.SOCK_STREAM shows the connection type which is TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# This is used to bind usually its a local host and 4 digits port number
s.bind((socket.gethostname(), 1234))
#The server will leave a que of five and will start listening
s.listen(5)

while True:
        
    print('Application started')
    #This Shows the application is listening for connections 
    print('socket is in listening state to %s:%d' % s.getsockname())
    #This will allow anybody to connect
    clientsocket, address = s.accept()
    #shows where the connection from
    print(f"connection from  {address} has been established!!")
    
    #This is used to make the interface easier for the user to read
    print("---------------------------------------------------") 
    
     
    print("SMTP Packet details:")
    #This will allow message to be sent to the client and inside there is the message detalis and type 
    clientsocket.send(bytes("220- Service Ready ", "utf-8"))
    
    #This Will allow recieve message from client
    recv1 = clientsocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != 'hello':
        print('')   
    #This will send 250 - ok to the client
    clientsocket.send(bytes(" 250 - ok ", "utf-8"))
    
    
    
    #This Will allow recieve message from client
    recv2 = clientsocket.recv(1024).decode()
    print(recv2)
    if recv2[:3] != '250':
        print('250 reply not received from server.')   
     
    
    #This Will allow recieve message from client    
    recv3 = clientsocket.recv(1024).decode()
     
    print("Client Mac Address:")
    print(recv3)
    if recv3[:3] != 'Mac':
         print('')
         
    #This Will allow recieve message from client     
    recv6 = clientsocket.recv(1024).decode()
    print("Client IP Address is:")
    print(recv6)
    if recv6[:3] != 'ip':
        print('')   
        
    #This Will allow recieve message from client
    recv4 = clientsocket.recv(1024).decode()
    
    print(recv4)
    if recv4[:3] != 'DATA':
         print('')
         
    clientsocket.send(bytes(" 345- Start mail input ", "utf-8"))
    print("---------------------------------------------------")

    

    #showing where the socket is bound to 
    print('socket is bound to %s:%d' % clientsocket.getsockname())
    
        

    #This Will allow recieve message from client
    recv5 = clientsocket.recv(1024).decode()
    print(recv5)
    if recv5[:3] != 'Quit':
        print('')
        
    #Closing the connection
    
    input("Please press Enter to terminate..")
    print('Closing the TCP socket...')
    clientsocket.close()
    print('CLOSED....')
    break
