#!/usr/bin/python3
"""INSERT ELEMENT INSIDE TABLE"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    connect = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=connect)
    new_session = Session()

    existing_state = new_session.query(State).filter
    (State.name == 'Louisiana').first()
    if not existing_state:
        add_to = State(name='Louisiana')
        new_session.add(add_to)
        new_session.commit()

    ret = new_session.query(State).filter(State.name == 'Louisiana').first()
    if ret:
        print(ret.id)
