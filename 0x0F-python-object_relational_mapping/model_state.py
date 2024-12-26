#!/usr/bin/python3
"""
model_state module
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()


class State(Base):
    """Creates a class State with and Table states in the
    hbtn_0e_6_usa database
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


engine = create_engine(
        "mysql+mysqldb://root:mySQLp%40ssword1@localhost:3306/hbtn_0e_6_usa")
Base.metadata.create_all(engine)
