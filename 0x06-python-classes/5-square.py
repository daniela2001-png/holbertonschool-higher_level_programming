#!/usr/bin/python3
"""
define a private instance object
and add a new methods
"""


class Square:
    """
    create a methods necessary
    """

    def __init__(self, size):
        """
        handling errors
        and asign the value to size
        """
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
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        method get of property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        method setter of the getter
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        print the size square
        """
        if (self.__size != 0):
            for i in range(self.__size):
                print('#'*self.__size)
        else:
            print()
