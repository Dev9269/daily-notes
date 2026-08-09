def box(text, w=60):
    border = '#' * w
    return '\n'.join([border, text.center(w), border])
