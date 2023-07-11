#!/usr/bin/python3
"""Function load_from_json_file"""
import json


def load_from_json_file(filename):
    """convert it into something can Pc Understand )"""
    with open(filename, "r", encoding='utf-8') as f:
        string = f.read()
        obj = json.loads(string)
        return obj
