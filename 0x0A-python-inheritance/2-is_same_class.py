#!/usr/bin/python3
"""
defino una funcion que verifica si
un objeto es instancia o no de una clase
"""


def is_same_class(obj, a_class):
    """
    función que retorna un bool
    """
    return(type(obj) is a_class)
