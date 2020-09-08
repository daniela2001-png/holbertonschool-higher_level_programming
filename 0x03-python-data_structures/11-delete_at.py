#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in my_list:
        if (idx == my_list.index(i)):
            my_list.remove(idx + 1)
    return (my_list)
