#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_cpy = a_dictionary.copy()
    return ({key: value * 2 for key, value in my_cpy.items()})
