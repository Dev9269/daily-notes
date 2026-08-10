import secrets

def random_token(n=32):
    return secrets.token_hex(n)

def api_key(prefix='sk_'):
    return prefix + secrets.token_urlsafe(24)
