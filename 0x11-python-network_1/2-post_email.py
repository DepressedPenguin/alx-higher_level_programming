#!/usr/bin/python3
"""Post with email"""
import urllib.request
import sys

if __name__ == "__main__":
    url_email = sys.argv[3]
    enc = url_email.encode('utf-8')
    request = urllib.request.Request(sys.argv[1], data=enc, method='POST')
    with urllib.request.urlopen(request) as re:
        content = re.read().decode('ascii')
        print(content)
