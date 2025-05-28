import yaml

def load_yaml(path: str):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def dump_yaml(obj, path: str):
    with open(path, 'w') as f:
        yaml.dump(obj, f, sort_keys=False)