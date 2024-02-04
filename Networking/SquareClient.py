import socket 
cs=socket.socket()
cs.connect(("localhost",9999))
print("CSP got connection from ssp")
val=input("Enter a value for getting its squre:")
cs.send(val.encode())
sdata=cs.recv(1024).decode()
print("Squre({})={}".format(val,sdata))
