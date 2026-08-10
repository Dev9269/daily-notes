import urllib.request

def get(url, timeout=10):
    req = urllib.request.Request(url, headers={'User-Agent': 'daily-notes'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read()
