def check(code):
    banned = ['eval(', 'exec(', 'pickle.loads']
    return [b for b in banned if b in code]
