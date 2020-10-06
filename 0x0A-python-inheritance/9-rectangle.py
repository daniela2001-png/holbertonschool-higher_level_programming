#!/usr/bin/python3

"""
class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    constructor de la clase
    """
    def __init__(self, width, height):
        """
        se inicializa los atributos
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """retorna el area d eun rectangulo"""
        return self.__width * self.__height

    def __str__(self):
        """metodo string"""
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
