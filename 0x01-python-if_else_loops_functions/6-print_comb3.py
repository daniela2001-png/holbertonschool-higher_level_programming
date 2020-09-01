#!/usr/bin/python3
for number in range(0, 8):
    for number_2 in range(number + 1, 10):
        print('{:d}{:d}'.format(number, number_2), end=', ')
print("{:d}{:d}".format(number + 1, number_2))
