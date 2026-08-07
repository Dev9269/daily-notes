import yaml

def load(path):
    with open(path) as f:
        return yaml.safe_load(f)

def get(cfg, key, default=None):
    return cfg.get(key, default)

def deep_get(cfg, keys, default=None):
    cur = cfg
    for k in keys:
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur
