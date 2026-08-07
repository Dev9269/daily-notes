import urllib.request

def probe(url, timeout=5):
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.status, dict(r.headers)
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers)

def check_dir(url, names):
    out = {}
    for n in names:
        status, _ = probe(url.rstrip('/') + '/' + n)
        out[n] = status
    return out
