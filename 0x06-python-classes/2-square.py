#!/usr/bin/python3
"""
define a private instance object
"""


class Square:
    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


"""
class Square:
    def __init__(self, size=0):
        if (type(size) is int):
            if (size >= 0):
                self.__size = size
            raise ValueError("value error")
        raise TypeError("TypeError")


class Square:
    def __init__(self, size=0):
        try:
            self.__size = size
        except ValueError:
            print("error1")
        except ValueError:
            print("error2")
        else:
            self.__size = size
"""
