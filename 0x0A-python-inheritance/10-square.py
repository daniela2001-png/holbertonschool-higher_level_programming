#!/usr/bin/python3
"""
clase square que hereda de recatngle
importamos nuestra clase padre Rectangle

"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ method area """
        return self.__size ** 2
