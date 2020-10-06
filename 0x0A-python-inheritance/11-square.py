#!/usr/bin/python3
"""
clase square que hereda de recatngle
importamos nuestra clase padre Rectangle

"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """constructor  d emi clase hija"""
    def __init__(self, size):
        """
        privado atributo size
        """
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """area de square"""
        return self.__size ** 2

    def __str__(self):
        """str method"""
        return("[Square] {}/{}".format(self.__size, self.__size))
