#!/usr/bin/python3
"""
11-model_state_insert
A scrpt that adds the State object "Louisiana" to the database
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
import sys

if __name__ == '__main__':
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3])
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name='Louisiana'))
    session.commit()

    state_id = session.query(State.id).filter_by(name='Louisiana').first()
    session.close

    for item in state_id:
        print(item)
