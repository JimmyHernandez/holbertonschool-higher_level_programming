#!/usr/bin/python3
"""_summary_ """
import json


def save_to_json_file(my_obj, filename):
    """
    Converting the string into a python object.
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
