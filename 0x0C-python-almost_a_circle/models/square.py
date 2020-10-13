#!/usr/bin/python3

"""

clase Rectangle que hereda de Base
cuando se desean atributos privados en una clase,
se deben delcarar e inicializar en el constructor _init_,
adicionalmente es necesario crear sus funciones
de getter(devulve el valor del atributo)
y setter(modifica el valor del atributo)
estos metodos acuden directamente al atributo,
pero de ahi en adelante la idea es llamar
a los atributos a partir de las funciones getter
y setter y no directamente al atributo
osea acceder a ellos como si fueran publicos
pero en realidad estamo accediendo es al setter o getter

"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    clase que hereda de Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        inicializo mis atributoscusando la lógica de mi
        metodo init padre!
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        retorna la representación string de la clase hija
        """
        return("[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width))

    @property
    def size(self):
        """
        retorno el valor modifacdo por el setter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        asigno el valor dado por el user
        """
        self.width = value

    def update(self, *args, **kwargs):
        """
        aqui sobrescribo mi metodo update
        con el de mi clase padre Rectangle
        """
        if args:
            if args is not None:
                lista = ["id", "size", "x", "y"]
                for i, j in zip(args, lista):
                    setattr(self, j, i)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
         retorno un diccionario de mi clase
        para mostrar sus atributos y valores de los mismos
        """
        x = super().to_dictionary()
        y = x.copy()
        y["size"] = self.width
        if y["height"] and y["width"]:
            del y["height"]
            del y["width"]
        return(y)
