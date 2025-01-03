#!/usr/bin/python3
"""
7-model_state_fetch_all module
A script that lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import Base, State
import sys


if __name__ == '__main__':
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3])
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    row = session.query(State).order_by(State.id).all()
    session.close()
    for item in row:
        print(f"{item.id}: {item.name}")
