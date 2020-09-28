#!/usr/bin/python3

"""class defined"""


class Rectangle:

    """class"""
    print_symbol = '#'
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """init"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """init"""
        return self.__width

    @width.setter
    def width(self, value):
        """init"""
        if (type(value) is not int):
            raise TypeError('width must be an integer')
        elif (value < 0):
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """init"""
        return self.__height

    @height.setter
    def height(self, value):
        """init"""
        if (type(value) is not int):
            raise TypeError('height must be an integer')
        elif (value < 0):
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """init"""
        return((self.__width) * (self.__height))

    def perimeter(self):
        """init"""
        r = ((self.__height + self.__height)+(self.__width + self.__width))
        if (self.__width == 0 or self.__height == 0):
            r = 0
        return r

    def __str__(self):
        """init"""
        string_to_print = ''
        if (self.__width != 0 and self.__height):
            string_to_print += "\n".join(str(self.print_symbol) * self.__width
                                         for j in range(self.__height))
        return string_to_print

    def __repr__(self):
        """init"""
        return("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """init"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
