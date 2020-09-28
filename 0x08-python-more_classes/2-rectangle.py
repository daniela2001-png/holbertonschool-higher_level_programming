#!/usr/bin/python3

""" define a class"""


class Rectangle:
    """init"""

    def __init__(self, width=0, height=0):
        """init"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """return value"""
        return self.__width

    @width.setter
    def width(self, value):
        """return value"""
        if (type(value) is not int):
            raise TypeError('width must be an integer')
        elif (value < 0):
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """return value"""
        return self.__height

    @height.setter
    def height(self, value):
        """return value"""
        if (type(value) is not int):
            raise TypeError('height must be an integer')
        elif (value < 0):
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """return value"""
        return((self.__width) * (self.__height))

    def perimeter(self):
        """return value"""
        r = ((self.__height + self.__height)+(self.__width + self.__width))
        if (self.__width == 0 or self.__height == 0):
            r = 0
        return r
