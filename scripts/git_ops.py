import subprocess

def sh(*args):
    r = subprocess.run(args, capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr

def short_log(n=10):
    return sh('git', 'log', '--oneline', f'-{n}')
