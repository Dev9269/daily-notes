import hashlib

def checksum(path, algo='sha256', chunk=1 << 20):
    h = hashlib.new(algo)
    with open(path, 'rb') as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()

def verify(path, expected, algo='sha256'):
    return checksum(path, algo) == expected.lower()
