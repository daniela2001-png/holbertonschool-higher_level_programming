#!/usr/bin/python3
'''
este modulo de python ejecuta mysqldb
para hacer querys y ejecutarlos desde un script
espero no sé me dificulte entender esto despues de 4 meses :v
'''
if __name__ == "__main__":

    import sys
    import MySQLdb
    ''' La secuencia de comandos debe tomar 3 argumentos: mysql username,\
    mysql password y databasename'''

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    '''
    nuestro query coincide con los ids de clave interna de states y
    clave externa en cities
    '''
    c.execute(
        "SELECT cities.name FROM cities\
        INNER JOIN states ON states.id = cities.state_id\
        WHERE states.name = %(states.name)s", {'states.name': sys.argv[4]})
    # obtenemos todos los objetos del query
    tuplas = c.fetchall()
    lista = []
    for row in tuplas:
        lista.append(row[0])
    '''
    join () es un método de cadena y devuelve una cadena
    en la que los elementos de la secuencia se han unido
    mediante un separador str
    '''
    print(", ".join(lista))

    '''
    Este método cierra el cursor y db,
    restablece todos los resultados y garantiza
    que el objeto del cursor no tenga ninguna referencia
    a su objeto de conexión original.
    '''
    c.close()
    db.close()
