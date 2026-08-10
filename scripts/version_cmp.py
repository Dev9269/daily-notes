def parse(v):
    return tuple(int(x) for x in v.split('.'))

def ge(a, b):
    return parse(a) >= parse(b)
