#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
    function that return a filename with meta utf8
    """
    with open(filename, 'r', encoding='utf8') as my_file:
        my_file_read = my_file.read()
        print(my_file_read)
