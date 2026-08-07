def gen(prefix, words):
    return [f'{prefix}{w}' for w in words]

def save(lines, path):
    with open(path, 'w') as f:
        f.write('\n'.join(lines))
