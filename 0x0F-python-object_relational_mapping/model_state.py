#!/usr/bin/python3
"""python file that """
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """class State"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
