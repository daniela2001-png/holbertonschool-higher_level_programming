#!/usr/bin/python3

"""define  class"""


class Rectangle:
    """init"""

    def __init__(self, width=0, height=0):
        """init"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """value"""
        return self.__width

    @width.setter
    def width(self, value):
        """value"""
        if (type(value) is not int):
            raise TypeError('width must be an integer')
        elif (value < 0):
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """value"""
        return self.__height

    @height.setter
    def height(self, value):
        """value"""
        if (type(value) is not int):
            raise TypeError('height must be an integer')
        elif (value < 0):
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """value"""
        return((self.__width) * (self.__height))

    def perimeter(self):
        """value"""
        r = ((self.__height + self.__height)+(self.__width + self.__width))
        if (self.__width == 0 or self.__height == 0):
            r = 0
        return r

    def __str__(self):
        """value"""
        string_to_print = ''
        if (self.__width != 0 and self.__height):
            string_to_print += "\n".join('#' * self.__width
                                         for j in range(self.__height))
        return string_to_print

    def __repr__(self):
        """value"""
        return("Rectangle({:d}, {:d})".format(self.__width, self.__height))
