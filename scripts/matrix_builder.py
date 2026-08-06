def matrix(versions, steps):
    return [{'py': v, 'step': s} for v in versions for s in steps]
