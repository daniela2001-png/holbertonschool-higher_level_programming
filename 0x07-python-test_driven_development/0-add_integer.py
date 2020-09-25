#!/usr/bin/python3
"""

Write a function that adds 2 integers

"""


def add_integer(a, b=98):
    """
    a & b can be int and if each one should be a float
    done a cast to int
    """
    if type(a) is int or type(a) is float:
        a = int(a)
    elif type(a) is str:
        raise TypeError("a must be an integer")
    else:
        raise TypeError("a must be an integer")
    if type(b) is int or type(b) is float:
        b = int(b)
    elif type(b) is str:
        raise TypeError("b must be an integer")
    else:
        raise TypeError("b must be an integer")
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
