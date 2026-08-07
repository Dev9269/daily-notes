def gen(prefix, words, upper=False):
    out = [f'{prefix}{w}' for w in words]
    if upper:
        out += [w.upper() for w in out]
    return out

def save(lines, path):
    with open(path, 'w') as f:
        f.write('\n'.join(lines))
