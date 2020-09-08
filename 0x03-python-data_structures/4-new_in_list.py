#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_list = my_list[:]
    for i in my_list:
        if (idx < 0):
            return (cpy_list)
        if (idx > len(my_list)):
            return (cpy_list)
        if (idx == cpy_list.index(i)):
            cpy_list.pop(idx)
            cpy_list.insert(idx, element)
            return (cpy_list)
