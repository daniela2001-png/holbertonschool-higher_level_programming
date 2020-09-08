#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    for letter in my_list:
        if (letter == 'c' or letter == 'C'):
            my_list.remove(letter)
        str_join = "".join(my_list)
        return (str_join)
