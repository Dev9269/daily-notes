import time
from functools import wraps

def retry(times=3, delay=1.0):
    def deco(fn):
        @wraps(fn)
        def inner(*a, **k):
            for i in range(times):
                try:
                    return fn(*a, **k)
                except Exception:
                    if i == times - 1:
                        raise
                    time.sleep(delay * (i + 1))
        return inner
    return deco
