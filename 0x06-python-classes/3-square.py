#!/usr/bin/python3
"""
define a private instance object
and add a new method instance area
"""


class Square:
    """
    define init and new method
    """

    def __init__(self, size):
        """
        evaluo los errores
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
        return (self.__size)**2
