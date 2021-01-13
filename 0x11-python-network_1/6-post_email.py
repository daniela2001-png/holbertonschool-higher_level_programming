#!/usr/bin/python3
"""
doing posts wiht requests
send a email to url
"""

import requests
from sys import argv

if __name__ == "__main__":
    my_post = requests.post(argv[1], data={'email': argv[2]})
    print(my_post.content.decode())
