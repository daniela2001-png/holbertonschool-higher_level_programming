#!/usr/bin/python3
"""clase Rectangle que hereda de Base
cuando se desean atributos privados en una clase,
se deben delcarar e inicializar en el constructor _init_,
adicionalmente es necesario crear sus
funciones de getter(devulve el valor del atributo)
y setter(modifica el valor del atributo),
estos metodos acuden directamente al atributo,
pero de ahi en adelante la idea es llamar
a los atributos a partir de las funciones getter
y setter y no directamente al atributo,
osea acceder a ellos como si fueran publicos
pero en realidad estamo accediendo es al setter o getter"""


from models.base import Base


class Rectangle(Base):
    """
    uso la funcion super para tomar la logica del init de la clase padre
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        heredo id del padre
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        return the value modificated
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter of width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        return the value modificated
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter of width
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        return the value modificated
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter of width
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        return the value modificated
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter of width
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        retorna el area de un rectangulo
        """
        return(self.width * self.height)

    def display(self):
        """
        muestra el ancho y largo representado por
        el simbolo "#" aun no usamos "x" o "y"
        """
        print((self.y) * "\n" + ((self.x) * " " + "#" * self.width + '\n')
              * self.height, end="")

    def __str__(self):
        """
        string format de mi subclase
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.x,
                                                                 self.y,
                                                                 self.width,
                                                                 self.height)

    def update(self, *args, **kwargs):
        """
        retrona ordenamente los atributos
        a traves de *args
        """
        if args:
            if args is not None:
                lista = ["id", "width", "height", "x", "y"]
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
        my_dict = {"id": self.id, "x": self.x, "y": self.y,
                   "height": self.height, "width": self.width}
        return my_dict
