#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in my_list:
        if (idx == my_list.index(i)):
            my_list.pop(idx)  # elimino el indice en dada posicion
            # inserto el nuevo elemento y lo reemplazo por el eliminado
            my_list.insert(idx, element)
            return (my_list)
        if (idx < 0):
            return (my_list)
        if (idx > len(my_list)):
            return (my_list)
