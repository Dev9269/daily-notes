import socket

def is_private(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        raise ValueError(ip)
    a = int(parts[0])
    return a == 10 or (a == 172 and 16 <= int(parts[1]) <= 31) or (a == 192 and parts[1] == '168')

def resolve(host):
    return socket.gethostbyname(host)
