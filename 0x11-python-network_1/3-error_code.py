#!/usr/bin/python3
"""
request url intranet with argv
using the module urllib
"""
from urllib import parse, request, error
from sys import argv

if __name__ == "__main__":
    try:
        url = argv[1]
        with request.urlopen(url) as response:
            result = response.read()
            print(result.decode())
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
