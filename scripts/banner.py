def box(text, w=60):
    border = '#' * w
    title = text.center(w)
    return f'{border}\n{title}\n{border}'

def shrink(text, w=60):
    return text[:w-3] + '...' if len(text) > w else text
