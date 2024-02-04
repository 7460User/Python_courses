import socket
ss=socket.socket()
ss.bind(("localhost",9999))
ss.listen(2)
print("ssp is ready to accept any csp Requrst")
while(True):
        try:
            cs,ca=ss.accept()
            csdata=cs.recv(1024).decode()
            print("val of client at server ={}".format(csdata))
            n=int(csdata)
            res=n*2
            cs.send(str(res).encode())
        except ValueError:
            cs.send("Don't enter strs ,alnums and symbols".encode())
            
