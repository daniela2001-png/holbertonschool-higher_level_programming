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
    # hacemos el query SQL a nuestra tabla state
    c.execute("""SELECT * FROM states
                ORDER BY states.id ASC""")
    # obtenemos todos los objetos del query
    for row in c.fetchall():
        print(row)

    '''
    Este método cierra el cursor y db,
    restablece todos los resultados y garantiza
    que el objeto del cursor no tenga ninguna referencia
    a su objeto de conexión original.
    '''
    c.close()
    db.close()
