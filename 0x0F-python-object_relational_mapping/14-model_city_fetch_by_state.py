#!/usr/bin/python3
"""
14-model_city_fetch_by_state
A script that prints all City Objects from the database hbtn_0e_14_usa
"""
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
import sys

if __name__ == '__main__':
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3])
            )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    row = session.query(
            City.id, State.name, City.name).join(City).order_by(City.id).all()
    session.close()
    for id, state, city in row:
        print(f'{state}: ({id}) {city}')
