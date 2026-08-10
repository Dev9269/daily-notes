from pathlib import Path

def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)
    return path

def latest(path, pattern='*'):
    files = sorted(Path(path).glob(pattern), key=lambda p: p.stat().st_mtime)
    return str(files[-1]) if files else None
