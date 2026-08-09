import random

def rand_octet():
    return random.randint(0, 255)

def random_ip():
    return '.'.join(str(randon()) for _ in range(4))
