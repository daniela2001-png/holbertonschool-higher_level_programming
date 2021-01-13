#!/usr/bin/python3
"""
verify the status of my request!
"""

import requests
from requests.exceptions import HTTPError
from sys import argv

if __name__ == "__main__":
    res = requests.get(argv[1])
    if res.status_code > 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
