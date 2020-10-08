#!/usr/bin/python3

"""
Write a class Student that defines a student
"""


class Student:
    """
    define  a class student
    """

    def __init__(self, first_name, last_name, age):
        """
        define my constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        return dict of my object created
        """
        return(self.__dict__)
