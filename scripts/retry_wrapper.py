import time
from functools import wraps

def retry(times=3, delay=1.0, backoff=2.0):
    def deco(fn):
        @wraps(fn)
        def inner(*a, **k):
            for i in range(times):
                try:
                    return fn(*a, **k)
                except Exception:
                    if i == times - 1:
                        raise
                    time.sleep(delay * (backoff ** i))
        return inner
    return deco
