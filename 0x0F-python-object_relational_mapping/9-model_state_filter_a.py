#!/usr/bin/python3
"""SHOW ALL RESULT THAT START WITH a"""
from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    connect = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping=True)
    Session = sessionmaker(bind=connect)
    new_session = Session()
    query_s = new_session.query(State).filter(
        State.name.like("%a%")).order_by(State.id.asc()).all()
    for x in query_s:
        print(x.id, x.name, sep=": ")
