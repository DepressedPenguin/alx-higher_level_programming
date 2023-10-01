#!/usr/bin/python3
"""Display The body of the request"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    args = sys.argv
    try:
        with urllib.request.urlopen(args[1]) as response:
            content = response.read().decode("utf-8")
            if 'Index' in content:
                print("Index")
            elif 'Error code: 401' in content:
                print("Error code: 401")
            elif 'Error code: 404' in content:
                print("Error code: 404")
            elif 'Error code: 500' in content:
                print("Error code: 500")
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
