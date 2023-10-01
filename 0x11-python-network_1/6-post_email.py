#!/usr/bin/python3
"""POST URL"""
import requests
import sys

if __name__ == "__main__":
    args = sys.argv
    data = {'email': args[2]}
    res = requests.post(args[1], data)
    print(res.text)
