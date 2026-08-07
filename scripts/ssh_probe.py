import socket

def banner(host, port=22, timeout=5):
    s = socket.create_connection((host, port), timeout)
    try:
        return s.recv(256).decode(errors='replace').strip()
    finally:
        s.close()
