#!/usr/bin/python3

"""
A simple script that defines a State class using SQLAlchemy \
    to represent a MySQL table.

The script connects to a MySQL server running on localhost\
    at port 3306 using SQLAlchemy.

All classes that inherit from Base must be imported before calling\
    Base.metadata.create_all(engine).
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents the 'states' table in the MySQL database.

    Attributes:
        id (int): Auto-generated, unique integer, can't be null,\
            and is a primary key.
        name (str): String with a maximum of 128 characters, can't be null.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
