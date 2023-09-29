#!/usr/bin/python3
"""fetch url"""
import urllib.request

if __name__ == "__main__"
url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as rr:
    data = rr.read()
    print("Body response:")
    print(f"    - type: {type(data)}")
    print(f"    - content: {data}")
    print(f"    - utf8 content: {data.decode('utf-8')}")
