import os
import shutil
import datetime
import glob

def rotate(path, max_bytes=10_000_000, keep=5):
    if os.path.getsize(path) < max_bytes:
        return
    ts = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    shutil.move(path, f'{path}.{ts}')
    olds = sorted(glob.glob(f'{path}.*'))
    for old in olds[:-keep]:
        os.remove(old)
