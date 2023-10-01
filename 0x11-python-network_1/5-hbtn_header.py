#!/usr/bin/python3
"""Fetches url"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    header_value = response.headers.get("X-Request-Id")

    if header_value is not None:
        print(header_value)
