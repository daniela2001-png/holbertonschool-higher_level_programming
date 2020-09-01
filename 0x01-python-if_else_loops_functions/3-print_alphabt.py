#!/usr/bin/python3
for each_letter in range(97, 123):
    if (each_letter == 101 or each_letter == 113):
        continue
    print(chr(each_letter), end='')
