#!/usr/bin/python3
"""DISPLAY BODY WITH REQUEST"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

        content = response.text
        print(content)

    except requests.exceptions.RequestException as e:
        print(f"Error code: {e.response.status_code}")
