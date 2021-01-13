#!/usr/bin/python3

"""
post to a url
and print some keys of a json
"""
import requests
import sys


def searchapi():
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    result = requests.post(
        "http://81d0e503c600.7b77981b.hbtn-cod.io:5000/search_user",
        data={"q": q})

    try:
        data = result.json()
        if data:
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No result")
    except:
        print("Not a valid JSON")


if __name__ == "__main__":
    searchapi()
