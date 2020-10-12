#!/usr/bin/python3

"""
clase Rectangle que hereda de Base

"""
from models.base import Base

class Rectangle(Base):
    """
    uso la funcion super para tomar la logica del init de la clase padre
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """return the value modificated"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        self.__width = value

    @property
    def height(self):
        """return the value modificated"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        self.__height = value

    @property
    def x(self):
        """return the value modificated"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """return the value modificated"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        self.__y = value
