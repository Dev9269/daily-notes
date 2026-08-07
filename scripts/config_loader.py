import yaml

def load(path):
    with open(path) as f:
        return yaml.safe_load(f)

def get(cfg, key, default=None):
    return cfg.get(key, default)
