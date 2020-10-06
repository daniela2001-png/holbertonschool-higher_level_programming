#!/usr/bin/python3
"""

funcion que vefirifica si un objeto es  eclase
independientemente de si hereda o no

"""


def inherits_from(obj, a_class):
    """

    uso el metodo isinstance()

    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
