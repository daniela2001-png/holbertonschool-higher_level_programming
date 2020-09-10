#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # recorro las keys ya que estas traen su respectivo valor
    for i in sorted(a_dictionary.keys()):
        print('{:s}: {}'.format(i, a_dictionary[i]))
