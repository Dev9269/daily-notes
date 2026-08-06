def check_endings(path):
    data = open(path, 'rb').read()
    return data.endswith(b'\n')
