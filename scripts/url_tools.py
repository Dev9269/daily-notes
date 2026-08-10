from urllib.parse import urlparse, urljoin

def base(url):
    p = urlparse(url)
    return f'{p.scheme}://{p.netloc}/'

def join(url, path):
    return urljoin(url, path)
