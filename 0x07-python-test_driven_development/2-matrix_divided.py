#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(matrix) is list:
        for element in matrix:
            if (type(element) is not list):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            else:
                for number in element:
                    if type(number) is int or type(number) is float:
                        return
                    else:
                        raise TypeError(
                            "matrix must be a matrix (list of lists) of integers/floats")
            new_list = (list(map((lambda columna: list(map((lambda x:
                                                            round(x/div, 2)), columna))), matrix)))
    else:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    return(new_list)
