#!/usr/bin/python3
"""
Write a function that reads n lines of a text file (UTF8)
and prints it to stdout:

"""


def read_lines(filename="", nb_lines=0):
    """
    reads n lines of a text file
    """
    with open(filename, 'r', encoding="utf8") as f:
        counter = 0
        for i in f:
            print(i, end="")
            counter = counter + 1
            if counter == nb_lines:
                break
