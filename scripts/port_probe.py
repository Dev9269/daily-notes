import socket

def probe(host, port, timeout=1.0):
    s = socket.socket()
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        return True
    except Exception:
        return False
    finally:
        s.close()

def scan(host, ports, timeout=1.0):
    return {p: probe(host, p, timeout) for p in ports}
