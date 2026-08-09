import time

def sleep_backoff(attempt, base=2.0):
    time.sleep(base * (1.5 ** attempt))
