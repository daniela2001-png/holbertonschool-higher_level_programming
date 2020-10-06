#!/usr/bin/python3
"""
clase con un metodo area(self)
"""


class BaseGeometry:
    """metodo publico que levanta un error"""
    def area(self):
        """se genera un raise"""
        raise Exception("area() is not implemented")
