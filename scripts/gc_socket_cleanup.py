def close_pending(loops):
    for loop in loops:
        if loop is not None:
            loop.close()
