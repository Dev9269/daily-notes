def read_ini(path):
    cfg = {}
    section = None
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line.startswith('[') and line.endswith(']'):
                section = line[1:-1]
                cfg[section] = {}
            elif '=' in line and section:
                k, v = line.split('=', 1)
                cfg[section][k.strip()] = v.strip()
    return cfg
