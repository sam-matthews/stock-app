import yaml

def open_yaml(yaml_config):
    with open(yaml_config, "r") as yamlfile:
        return yaml.safe_load(yamlfile)
        