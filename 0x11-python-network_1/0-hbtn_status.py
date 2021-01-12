#!/usr/bin/python3
from urllib import request

with request.urlopen('https://intranet.hbtn.io/status') as response:
    result = response.read()
    h = "Body response:\n\t" \
        "- type: {}\n\t" \
        "- content: {}\n\t" \
        "- utf8 content: {}"
    print(h.format(type(result), result, result.decode()))
