#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    largo = len(argv)
    if (largo > 2):
        print("{:d} arguments:".format(len(argv) - 1))
        for i, j in enumerate(argv):
            if (i != 0):
                print("{:d}: {:s}".format(i, j))
    if (largo == 1):
        print("0 arguments.")
    if (largo == 2):
        print('1 argument:')
        print("1: {:s}".format(argv[1]))
