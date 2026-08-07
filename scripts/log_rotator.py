import os
import shutil
import datetime

def rotate(path, max_bytes=10_000_000):
    if os.path.getsize(path) < max_bytes:
        return
    ts = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    shutil.move(path, f'{path}.{ts}')
