#!/usr/bin/python3
"""
using the module requests
"""
import requests

if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    print('Body response:\n'f'\t- type: {type(response.content.decode())}'
          '\n'f'\t- content: {response.content.decode()}')
