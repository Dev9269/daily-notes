import fnmatch
import os

def grepp(root, term, pattern='*'):
    hits = []
    for dirpath, _, names in os.walk(root):
        for name in names:
            if not fnmatch.fnmatch(name, pattern):
                continue
            path = os.path.join(dirpath, name)
            try:
                for i, line in enumerate(open(path, encoding='utf-8', errors='replace'), 1):
                    if term in line:
                        hits.append((path, i, line.strip()[:80]))
            except OSError:
                pass
    return hits
