#!/usr/bin/python3

"""
creo una clase padre llamada Base
"""

class Base:
    """
    creo una instacia de clase privada
    e iniciclaizo con el constructor mis objetos
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        inicializo el objeto id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
