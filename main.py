import socket
def open_port(port):

    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#ipv4 and tcp

    sock.bind(("localhost",port))#socket binding to the network
    sock.listen(1)#open socket and 1 can connect
    sock.close()#close socket
open_port(1111)