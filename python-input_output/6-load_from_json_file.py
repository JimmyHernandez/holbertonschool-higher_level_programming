#!/usr/bin/python3
"""_summary_ """
import json


def load_from_json_file(filename):
    """
    Converting the string into a python object.
    """
    with open(filename, 'r') as f:
        return json.loads(f.read())
