#!/usr/bin/python3
"""
using the module requests
"""


if __name__ == "__main__":
    import requests
    response = requests.get("https://intranet.hbtn.io/status")
    # print('Body response:\n'f'\t- type: {type(response.content.decode())}'
    #       '\n'f'\t- content: {response.content.decode()}')
    h = "Body response:\n\t" \
        "- type: {}\n\t" \
        "- content: {}"
    print(h.format(type(response.content.decode()), response.content.decode()))
