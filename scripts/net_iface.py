import socket

def local_ips():
    hostname = socket.gethostname()
    return socket.gethostbyname_ex(hostname)[2]
