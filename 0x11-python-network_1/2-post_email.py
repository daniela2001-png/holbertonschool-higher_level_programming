#!/usr/bin/python3
"""
request url intranet with argv
using the module urllib
"""
from urllib import parse, request
from sys import argv

if __name__ == "__main__":
    data = parse.urlencode({'email': argv[2]})
    url = argv[1]
    data = data.encode("utf-8")
    with request.urlopen(url, data) as response:
        result = response.read()
        print(result.decode())
