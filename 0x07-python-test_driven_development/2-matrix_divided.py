#!/usr/bin/python3
"""
Function that divides a matrix (list with sublist)
each number shoul be a integer or float
"""


def matrix_divided(matrix, div):
    """
    give a number with your respective number to divide
    """
    e = 'matrix must be a matrix(list of lists) of integers/floats'
    if type(matrix) is not list or len(matrix) == 0 or type(matrix[0])\
            is not list:
        raise TypeError(
            "matrix must be a matrix(list of lists) of integers/floats")
    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    size = len(matrix[0])
    for columna in matrix:
        if size != len(columna):
            raise TypeError(
                "Each row of the matrix must have the same size")
        if type(columna) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for numero in columna:
            if type(numero) is not float and type(numero) is not int:
                raise TypeError(e)
    new_list = (list(map((lambda columna: list(map((lambda x:
                round(x/div, 2)), columna))), matrix)))
    return(new_list)
