import socket

import sys_logging

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
# This actively initiates TCP server connection.
my_socket.connect((host, port))
# This receives the TCP message.
msg = my_socket.recv(1024)
my_socket.close()
sys_logging.info(msg.decode('ascii'))
