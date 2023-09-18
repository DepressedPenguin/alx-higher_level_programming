#!/usr/bin/python3
"""Find Any Match  """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys

if __name__ == "__main__":
    connect = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=connect)
    new_session = Session()
    name_arg = sys.argv[4]
    Find_state = new_session.query(State).filter(
            State.name.like(name_arg)).first()
    if Find_state:
        print(Find_state.id)
    else:
        print("Not found")
