#!/usr/bin/python3
"""Write into file and count chars"""


def write_file(filename="", text=""):
    """Function to write into a file"""
    with open(filename, "w", encoding='utf-8') as file:
        file.write(text)
        return file.tell()
