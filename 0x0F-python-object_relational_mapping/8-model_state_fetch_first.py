#!/usr/bin/python3
"""show first result from table"""
from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    connect = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3],), pool_pre_ping=True)
    Session = sessionmaker(connect)
    new_session = Session()
    first_result = new_session.query(State).first()
    if not first_result:
        print("Nothing")
    else:
        print(first_result.id, first_result.name, sep=': ')
