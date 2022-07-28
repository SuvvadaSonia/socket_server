import socket
s = socket.socket()
h=socket.gethostname()
s.connect((h,9999))
print(s.recv(1024))
