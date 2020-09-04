#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    suma = 0
    for i in argv:
        if (i != argv[0]):  # aqui estoy comparando un str por eso uso argv[0]
            suma += int(i)
    print(suma)
