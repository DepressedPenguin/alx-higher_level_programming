#!/usr/bin/python3
"""Post meth with Email """

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)

    content = response.text
    print("Your email is:", content)
