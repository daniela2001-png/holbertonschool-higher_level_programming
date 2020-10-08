#!/usr/bin/python3
"""
Write a function that returns the number of lines of a text file:


"""


def number_of_lines(filename=""):
    """
    funciton that return the number of a file
    """
    with open(filename, 'r') as file:
        return len(file.readlines())
