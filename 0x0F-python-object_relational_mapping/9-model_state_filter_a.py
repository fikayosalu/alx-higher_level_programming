#!/usr/bin/python3
"""
9-model_state_filter module
A script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3])
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).filter(
            State.name.like("%a%")).order_by(State.id).all()
    session.close()

    for items in row:
        print(f"{items.id}: {items.name}")
