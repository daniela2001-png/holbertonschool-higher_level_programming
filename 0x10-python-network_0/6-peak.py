#!/usr/bin/python3
"""I have been thinking but i can not do it
in other way :() """


def find_peak(list_of_integers):
    """
    function that founds the peak in a list
    """
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
