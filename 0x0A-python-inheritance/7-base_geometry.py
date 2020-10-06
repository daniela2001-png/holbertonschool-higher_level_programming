#!/usr/bin/python3

"""
clase con un metodo area(self)
"""


class BaseGeometry:
    """metodo publico que levanta un error"""
    def area(self):
        """se genera un raise"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validar value"""
        if type(value) != int:
            raise TypeError(str(name) + " must be an integer")
        if value <= 0:
            raise ValueError(str(name) + " must be greater than 0")
