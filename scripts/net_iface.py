import socket

def local_ips():
    hostname = socket.gethostname()
    return socket.gethostbyname_ex(hostname)[2]

def is_private(ip):
    return ip.startswith(('10.', '192.168.')) or ip.startswith('172.') and 16 <= int(ip.split('.')[1]) <= 31
