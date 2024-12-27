#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Fetch arguments: username, password, database name
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """
    # Create the database engine
    engine = create_engine(
    f"mysql+mysqlconnector://{username}:{password}@localhost:3306/{database}")
    """
    # Create a configured "Session" class and an instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects, ordered by id
    states = session.query(State).order_by(State.id).all()

    # Print each state in the required format
    for state in states:
        print(f"{state.id}: {state.name}")
