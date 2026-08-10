def stats(text):
    words = text.split()
    return {'chars': len(text), 'words': len(words),
            'lines': text.count('\n') + 1,
            'unique': len(set(words))}
