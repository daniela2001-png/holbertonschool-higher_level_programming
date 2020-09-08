#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        final = sorted(my_list)
        return(final[-1])
    else:
        return (None)
