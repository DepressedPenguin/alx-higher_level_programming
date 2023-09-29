#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as rep:
    body = rep.read()
    utf = body.decode('utf-8')
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", utf)
