# 0x0C. Python - Almost a circle

--------------------------

![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)

--------------------------

## Example

--------------------------

- Write the first class Base:

<b>1</b> - Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python module

<b>2</b> - Create a file named models/base.py:

- Class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)::
if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
otherwise, increment __nb_objects and assign the new value to the public instance attribute id
--------------------------

<b>This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)

--------------------------

    #!/usr/bin/python3

    """
    creo una clase padre llamada Base
    """


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



--------------------------

## By: <a href="https://github.com/daniela2001-png">Daniela Morales</a> 😎


--------------------------
