#!/usr/bin/python3
"""
13-model_state_delete_a
A script that deletes all State objects with a name containing letter
'a' from the database hbtn_0e_6_usw
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

    session.query(State).filter(State.name.like('%a%')).delete()
    session.commit()
    session.close()
