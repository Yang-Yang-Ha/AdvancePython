import socket

import sys_logging

my_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# This returns the hostname.
host = socket.gethostname()
port = 9999
# This binds the address to the socket. This address holds the hostname and the port number pair.
my_server.bind((host, port))
# This starts the TCP listener.
my_server.listen(5)

while True:
    my_client, addr = my_server.accept()
    sys_logging.info(f'connect to {str(addr)}')
    # This sends the TCP message.
    my_client.send(bytes('hi', 'ascii'))
    my_client.close()
