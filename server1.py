"""
Description: A simple connection between socket server and socket client
using socket module
Author: Sonia
Position: Junior Software Engineer

"""

import socket # import the socket module


s=socket.socket() # create a socket object
h=socket.gethostname() # Get local machine name
s.bind((h,9999)) # Reserve a port for your service and bind to that particular port
s.listen(3) # Now wait for client connection

while True:
    c,addr = s.accept() # Establish connection with client
    print("Got connection from ",addr)
    c.send(b'Thank you for connecting') # Send message to client after connection
    c.close() # close the connection
    