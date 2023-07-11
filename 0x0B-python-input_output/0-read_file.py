#!/usr/bin/python3
"""function read from file"""


def read_file(filename=""):
    """read from txt file"""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
