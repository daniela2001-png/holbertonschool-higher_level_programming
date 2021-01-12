#!/usr/bin/python3
"""
request url intranet with argv
using the module urllib
"""


from urllib import request
from sys import argv

with request.urlopen(argv[1]) as response:
    result = response.info()
    print(result.get("X-Request-Id"))
