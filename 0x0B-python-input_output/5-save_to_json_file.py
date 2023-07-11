#!/usr/bin/python3
"""Function save_to_json"""


import json


def save_to_json_file(my_obj, filename):
    """Function that writes with JSON inside a file"""
    with open(filename, "w", encoding="utf-8") as f:
        string = json.dumps(my_obj)
        f.write(string)
