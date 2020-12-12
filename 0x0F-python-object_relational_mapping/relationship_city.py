#!/usr/bin/python3
'''
contenga la definición de clase de a State
y una instancia Base = declarative_base()

'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    '''
    la clase City al igual que le resto heredaran
    de Base
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
