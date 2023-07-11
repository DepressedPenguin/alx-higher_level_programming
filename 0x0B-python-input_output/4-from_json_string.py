#!/usr/bin/python3
"""Function json_string"""
import json


def from_json_string(my_str):
    """loads from file"""
    string = json.loads(my_str)
    return string
