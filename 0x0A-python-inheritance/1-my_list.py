#!/usr/bin/python3

"""
clase que hereda de la clase padre list

"""


class MyList(list):
    """
    clase hija
    """

    def print_sorted(self):
        """metodo publico que organiza una lista"""
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
