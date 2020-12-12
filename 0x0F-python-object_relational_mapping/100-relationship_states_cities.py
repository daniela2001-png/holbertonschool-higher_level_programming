#!/usr/bin/python3
'''
addig california to state and
san francisco to city :3
'''

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    '''
    COMO YA SABEMOS LA CLASE STATE ES QUIEN GUARDA LA RELACION
    CON LA CLASE CITY ENTONCES CREAMOS UNA ISNTANCIA DE CLASE STATE
    PARA LLAMAR LUEGO LA RELACION DE cities  Y ALLI
    PASARLE EL NOMBRE QUE QUEREMOS INSERTAR
    '''
    state = State(name="California", cities=[City(name="San Francisco")])
    session.add(state)
    session.commit()
    session.close()
