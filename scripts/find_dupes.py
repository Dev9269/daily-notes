import hashlib
from collections import defaultdict

def dupes(root, algo='sha256'):
    seen = defaultdict(list)
    for dirpath, _, names in os.walk(root):
        for name in names:
            path = os.path.join(dirpath, name)
            try:
                h = hashlib.new(algo, open(path, 'rb').read()).hexdigest()
                seen[h].append(path)
            except OSError:
                pass
    return {k: v for k, v in seen.items() if len(v) > 1}
