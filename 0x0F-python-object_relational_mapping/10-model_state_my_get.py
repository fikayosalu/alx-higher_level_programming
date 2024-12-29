#!/usr/bin/python3
"""
10-model_state_my_get
A script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
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

    state_id = session.query(State.id).filter_by(name=sys.argv[4]).first()
    session.close()

    if state_id:
        for items in state_id:
            print(items)
    else:
        print('Not found')
