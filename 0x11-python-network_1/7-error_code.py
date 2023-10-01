#!/usr/bin/python3
"""POST WITH REQUEST"""
import requests
import sys

if __name__ == "__main__":
    args = sys.argv
    try:
        response = requests.get(args[1])
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as exception:
        print(f"Error code: {exception.response.status_code}")
