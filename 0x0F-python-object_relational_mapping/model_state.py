#!/usr/bin/python3
'''
contenga la definición de clase de a State
y una instancia Base = declarative_base()

'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class State(Base):
    '''
    la clase State al igual que le resto heredaran
    de Base
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
