#!/usr/bin/env python3
# the statement above is called a shebang,this statement tells the interpretor that this module should be interpreated asna script. this however can affect import statements in large ptyhon projects.

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base() # note that inheritance of declarative_base from Base helps us avoid re-writing code.
# also note that Base is a parent object. 
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key= True)
    name = Column(String())

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine) # the create_all() in this line tells the engine that all models that inherit from base are to create tables.