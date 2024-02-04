import socket,sys
while(True):
    s=socket.socket()
    s.connect( ("127.0.0.1",9999) )
    csdata=input("Student-->")
    if(csdata.lower()=="bye"):
        s.send("by girlfriend,i have some works!".encode())
        sys.exit()
    else:
        s.send(csdata.encode())
        ssdata=s.recv(1024).decode()
        print("girls-->{}".format(ssdata))
        