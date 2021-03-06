import socket               # Import socket module

def sendFile(filepath):
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 12345                 # Reserve a port for your service.

    s.connect((host, port))
    f = open(filepath,'rb')
    print ('Sending...')
    l = f.read(1024)
    while (l):
        print ('Sending...')
        s.send(l)
        l = f.read(1024)
    f.close()
    print ("Done Sending")
    print (s.recv(1024))
    s.close