"""
Description: A simple connection between socket server and socket client
using socket module
Author: Sonia
Position: Junior Software Engineer

"""

import socket # import a socket module


s = socket.socket() # create a socket object
h=socket.gethostname() # get the local machine name
s.connect((h,9999)) # reserve a port for your connection service and connects to that 
print(s.recv(1024))
s.close() # close the socket when done