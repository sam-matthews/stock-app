import json

def open_json(json_file):
    with open(json_file, 'r') as json_file:
        return json.load(json_file)