#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) >= ord('a') and ord(i) <= ord('z')):
            mayuscula = (chr(ord(i) - 32))
        else:
            mayuscula = i
        print('{:s}'.format(mayuscula), end='')
    print()
