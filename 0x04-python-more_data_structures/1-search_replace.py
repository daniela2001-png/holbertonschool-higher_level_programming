#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copia = my_list[:]
    for i in range(0, len(copia)):
        if copia[i] == search:
            copia.pop(i)
            copia.insert(i, replace)
    return (copia)
