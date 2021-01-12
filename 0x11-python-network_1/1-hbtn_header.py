#!/usr/bin/python3
from urllib import request
from sys import argv
"""
request url intranet with argv
using the module urllib
"""
with request.urlopen(argv[1]) as response:
    result = response.info()
    print(result.get("X-Request-Id"))
