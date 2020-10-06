# HERENCIA EN PYTHON

## Ejemplo

 
  
    class Pais():
        def __init__(self, nombre, presidente):
            self.nombre = nombre
            self.presidente = presidente
        def __str__(self):
            return ("Pais: {} - Presidente {}".format(self.nombre, self.presidente))
    class Ciudad():
        def __init__(self, nombre_ciudad, habitantes, pais):
            self.nombre_ciudad = nombre_ciudad
            self.habitantes = habitantes
            self.pais = pais1

        def __str__(self):
            return("Nombre Ciudad: {} - Numero de habitantes {} - {}".format(self.nombre_ciudad, self.habitantes, self.pais))

    pais1 = Pais("Colombia", "None")
    print(pais1)
    ciudad1 = Ciudad("Bogota", "18928", pais1)
    print(ciudad1)

## Salida
`

    Pais: Colombia - Presidente None
    Nombre Ciudad: Bogota - Numero de habitantes 18928 - Pais: Colombia - Presidente None

`

## Hecho por: <a href= "https://github.com/daniela2001-png">Daniela morales 🤗 