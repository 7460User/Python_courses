import socket
s=socket.socket()
s.bind( ("127.0.0.1",9999) )
s.listen(1)
print("SSP is ready to accept any CSP:")
print("-"*50)
while(True):
    cs,ca=s.accept()
    csdata=cs.recv(1024).decode()
    print("Student Msg--->{}".format(csdata))
    sdata=input("girlfriend-->")
    cs.send(sdata.encode())
