#!/usr/bin/python3

"""
creo una clase padre llamada Base
"""
import json


class Base:
    """
    creo una instacia de clase privada
    e iniciclaizo con el constructor mis objetos
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        inicializo el objeto id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        retorna un json de los dicts
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        vamos a sobrescribir en un json los dicts de mis clases hijas
        type <'str'>
        """
        my_lists_dict = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for i in list_objs:
                # aqui creo mi lista de dicts
                my_lists_dict.append(cls.to_dictionary(i))
        lista_dict = cls.to_json_string(my_lists_dict)
        with open(filename, "w", encoding="UTF-8") as f:
            f.write(lista_dict)

    @staticmethod
    def from_json_string(json_string):
        """
        convertimos de json string a una lista de dicts
        mejor dicho pasamos de type<'str'> a type<'list'>
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        metodo devuelve una instancia con todos los atributos ya establecidos:
        el **dictionary sera nuestro kwargs para el metodo to dictionary()

        """
        # creo el dummy que sera la instacia fictisia de mi clase
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 4)
        elif cls.__name__ == "Square":
            dummy = cls(3, 4)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        retornamos una lista de instancias de la clase actual
        """
        my_list = []
        try:
            filename = cls.__name__ + ".json"
            with open(filename, "r") as f:
                x = cls.from_json_string((f.read()))
                for i in x:
                    my_list.append(cls.create(**i))
            return my_list
        except:
            return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        csv loader
        """
        my_lists_dict = []
        filename = cls.__name__ + ".csv"
        if list_objs is not None:
            for i in list_objs:
                # aqui creo mi lista de dicts
                my_lists_dict.append(cls.to_dictionary(i))
        lista_dict = cls.to_json_string(my_lists_dict)
        with open(filename, "w", encoding="UTF-8") as f:
            f.write(lista_dict)

    @classmethod
    def load_from_file_csv(cls):
        """
        load file csv
        """
        my_list = []
        try:
            filename = cls.__name__ + ".csv"
            with open(filename, "r") as f:
                x = cls.from_json_string((f.read()))
                for i in x:
                    my_list.append(cls.create(**i))
            return my_list
        except:
            return my_list
