import random

def random_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

def random_mac():
    return ':'.join(f'{random.randint(0,255):02x}' for _ in range(6))
