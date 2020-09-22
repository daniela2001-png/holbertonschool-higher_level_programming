#!/usr/bin/python3
"""
define a private instance object
and add new methods
"""


class Square:
    """
    declare the methods necessary
    """

    def __init__(self, size, position=(0, 0)):
        """
        constructor handling erros
        """
        self.__position = position
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        return the area of a square
        """
        return (self.__size)**2

    @property
    def size(self):
        """
        method getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        method setter
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        print the tuple coordinates and the size of teh square
        """
        if (self.__size != 0):
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(' '*self.__position[0] + '#' * self.__size)
        else:
            print()

    @property
    def position(self):
        """
        getter to position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter to position
        """
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                    return
        raise TypeError("position must be a tuple of 2 positive integers")
