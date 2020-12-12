#!/usr/bin/python3
'''
enumere todos los State objetos de la base de datoshbtn_0e_6_usa
'''

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys
if __name__ == "__main__":
    '''
    en este punto creamos el engine a nuetsra base de datos mysqldb
    tomado el input con argv[] y creamos el session instance
    '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # creamos nuestro objeto sesisonmarker
    Session = sessionmaker(bind=engine)
    session = Session()
    # obtenemos los nombres de esstado que concidan con el argv
    # y si es asi imprimimos el id de ese estado
    result = session.query(State).filter(State.name == sys.argv[4]).one()
    if (result):
        print("{}".format(result.id))
    else:
        print("Not found")
    session.close()
