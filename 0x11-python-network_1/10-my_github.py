#!/usr/bin/python3
"""
Do requests to API github
"""

from requests.auth import HTTPBasicAuth
import requests
from sys import argv

response = requests.get(
    "https://api.github.com/users/{}".format(argv[1]),
    auth=HTTPBasicAuth(argv[1], argv[2]))

print(response.json().get("id"))
