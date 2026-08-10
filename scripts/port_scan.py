import socket

def scan(host, ports, timeout=0.5):
    open_ports = []
    for port in ports:
        s = socket.socket()
        s.settimeout(timeout)
        try:
            s.connect((host, port))
            open_ports.append(port)
        except OSError:
            pass
        finally:
            s.close()
    return open_ports

def scan_range(host, low=1, high=1024, timeout=0.5):
    return scan(host, range(low, high + 1), timeout)
