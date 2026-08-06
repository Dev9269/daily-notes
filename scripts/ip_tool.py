def is_private(ip):
    return ip.startswith('10.') or ip.startswith('192.168.')
