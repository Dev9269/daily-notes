import socket

def resolve(name):
    try:
        return socket.gethostbyname_ex(name)
    except socket.gaierror:
        return None

def walk(base, count):
    out = {}
    for i in range(count):
        ip = resolve(f'{i}.{base}')
        if ip:
            out[i] = ip
    return out
