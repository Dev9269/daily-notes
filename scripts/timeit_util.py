import time
from functools import wraps

def timed(fn):
    @wraps(fn)
    def inner(*a, **k):
        t0 = time.perf_counter()
        try:
            return fn(*a, **k)
        finally:
            print(f'{fn.__name__} took {time.perf_counter() - t0:.3f}s')
    return inner
