# This module is used to store the main functions which get called.

import modules.app_yaml as app_yaml

def heading():
    config = app_yaml.open_yaml("config.yaml")

    print("app_name: " + config["app_name"])
    print("version:  " + str(config["version"]))

