import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow reuse of address
s.bind(("127.0.0.1", 9999))  # Use the same or a different port
s.listen(1)
print("SSP is ready to accept any CSP:")
print("-" * 40)

while True:
    cs, ca = s.accept()
    csdata = cs.recv(1024).decode()
    print("Student Msg --> {}".format(csdata))
    sdata = input("KVR --> ")
    cs.send(sdata.encode())
