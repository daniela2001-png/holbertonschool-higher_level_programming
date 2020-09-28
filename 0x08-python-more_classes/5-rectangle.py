#!/usr/bin/python3
"""
create a Rectangle class
"""


class Rectangle:
    """
    define the methods in a new class
    """

    def __init__(self, width=0, height=0):
        """
        init the objects in the constructor
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """return the value given by the setter"""
        return self.__width

    @width.setter
    def width(self, value):
        """process the value to get"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """return the value given by the setter"""
        return self.__height

    @height.setter
    def height(self, value):
        """process the value to get """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """method that returns the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            p = 0
        p = (2*self.__width) + (2*self.__height)
        return (p)

    def __str__(self):
        """method string"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return(('#' * self.__width + '\n') * self.__height)

    def __repr__(self):
        """return a string representation of the rectangle"""
        return("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """delete a class"""
        print("Bye rectangle...")
