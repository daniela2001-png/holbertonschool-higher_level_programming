#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # me recorre cada lista
    for i in matrix:
        # me recorre cada lista de lista
        print(" ".join('{:d}'.format(j) for j in i))
