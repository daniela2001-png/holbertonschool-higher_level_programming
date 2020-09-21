#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    my_list = []
    final = 0
    for i in range(list_length):
        try:
            final = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            final = 0
        except ZeroDivisionError:
            print("division by 0")
            final = 0
        except TypeError:
            print("wrong type")
            final = 0
        finally:
            my_list.append(final)
    return my_list
