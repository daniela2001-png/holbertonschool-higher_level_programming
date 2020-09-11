#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    else:
        my_dict = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        var = 0
        for i in range(len(roman_string)):
            # aqui valido cuanod sea la primera letra
            if (i == 0):
                var += my_dict[roman_string[i]]
            # aqui valido si el numero anterior es mayor o menor
            elif (my_dict[roman_string[i - 1]] < my_dict[roman_string[i]]):
                var -= my_dict[roman_string[i - 1]] * 2
                var += my_dict[roman_string[i]]
            else:
                var += my_dict[roman_string[i]]
    return (var)
