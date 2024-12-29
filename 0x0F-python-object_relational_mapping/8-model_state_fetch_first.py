#!/usr/bin/python3
"""
8-model_state_fetch_first module
A script that prints the first State Object from the database hbtn_0e_6_usa
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
    row = session.query(State).order_by(State.id).first()
    session.close()

    if row is None:
        print('Nothing')
    else:
        print(f"{row.id}: {row.name}")
