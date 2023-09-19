#!/usr/bin/python3
"""Change State Name"""
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    connect = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    new_session = sessionmaker(bind=connect)
    session = new_session()
    state_to_update = session.query(State).filter(State.id == 2).first()

    state_to_update.name = 'New Mexico'
    session.commit()
    "print(state_to_update.name)"
