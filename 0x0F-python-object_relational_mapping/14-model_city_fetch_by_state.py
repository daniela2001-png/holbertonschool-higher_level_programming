#!/usr/bin/python3
'''
adding class city with a relationship
with state.id
'''
from model_city import City, Base
from model_state import State
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
    a = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()
    for city, state in a:
        print("{}: ({}) {}".format(city.name, state.id, state.name))
    session.close()
