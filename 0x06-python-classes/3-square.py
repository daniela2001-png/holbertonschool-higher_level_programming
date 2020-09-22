#!/usr/bin/python3
"""
    this class is empty
"""


class Square:
    """
        this class contains a unique private
        attribute because the theme of
        perimeter areas of a square is essential


    """

    def __init__(self, size=0):
        """This init contains:
    instance private attribute (object)

    it is called: size and is a integer

    Return Value: None """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif(size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
# size is the value of the instance
# Instead be a instance!

    def area(self):
        """Method od Instance public that takes a object"""
        return(self.__size) ** 2