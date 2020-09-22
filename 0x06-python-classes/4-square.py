#!/usr/bin/python3
"""
define a private instance object
use decorator property y setter

"""


class Square:
    """
    define a new methods
    """

    def __init__(self, size=0):
        """
        start instances
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        retorno el area del cuadrado
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """
        get the values of setter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        modify the value
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
