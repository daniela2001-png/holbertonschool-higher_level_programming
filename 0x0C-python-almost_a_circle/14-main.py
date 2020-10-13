#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

    #r1 = Rectangle(0, 1)
    dictionary = {}
    json_dictionary = Base.to_json_string([])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary) #aqui caundo ejecuta esta linea deberia parcerme el "[]"
    print(type(json_dictionary))
