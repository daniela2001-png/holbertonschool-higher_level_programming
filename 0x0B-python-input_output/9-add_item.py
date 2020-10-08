#!/usr/bin/python3

"""
a script that adds all arguments to a Python list, and then save them to a file

"""


from sys import argv

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


filename = "add_item.json"


try:
    lol = load_from_json_file(filename)
except Exception as e:
    lista = []

"""aqui escribo sobre la lista sin modificarla"""
save_to_json_file(argv[1:] + lol, filename)
