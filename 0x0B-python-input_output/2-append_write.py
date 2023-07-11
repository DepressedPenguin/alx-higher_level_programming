#!/usr/bin/python3
"""Function that appends"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file"""
    with open(filename, "a", encoding="utf-8") as calimero_file:
        calimero_file.write(text)
        return calimero_file.tell()
