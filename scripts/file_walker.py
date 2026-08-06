import os

def walk(root, ext):
    hits = []
    for dirpath, dirnames, filenames in os.walk(root):
        for name in filenames:
            if name.endswith(ext):
                hits.append(os.path.join(dirpath, name))
    return sorted(hits)

def count(root, ext):
    return len(walk(root, ext))
