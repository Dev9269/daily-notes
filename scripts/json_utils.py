import json

def load(path):
    with open(path) as f:
        return json.load(f)

def dump(obj, path, pretty=True):
    with open(path, 'w') as f:
        json.dump(obj, f, indent=2 if pretty else None)
