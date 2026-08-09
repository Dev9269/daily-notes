import time

def sleep_backoff(attempt, base=2.0):
    time.sleep(base * (1.5 ** attempt))

def jitter(seconds, spread=0.2):
    import random
    return seconds * (1 + random.uniform(-spread, spread))
