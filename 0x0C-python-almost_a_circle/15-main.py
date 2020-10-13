#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10000, 7)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([])

    with open("Rectangle.json", "r") as file:
        print(file.read())

