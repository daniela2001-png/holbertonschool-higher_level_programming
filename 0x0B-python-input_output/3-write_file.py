#!/usr/bin/python3
"""

Write a function that writes a string to a text file (UTF8)
and returns the number of characters written:

"""


def write_file(filename="", text=""):
    """
    wrtie over a filename in format utf8
    """
    with open(filename, "w", encoding="utf8") as f:
        return f.write(text)
