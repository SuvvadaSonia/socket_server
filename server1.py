import socket
s=socket.socket()
h=socket.gethostname()
s.bind((h,9999))
s.listen(3)
while True:
    c,addr = s.accept()
    print("Got connection from ",addr)
    c.send(b'Thank you for connecting')
    c.close()
    