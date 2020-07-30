from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,MetaData
from sqlalchemy.ext.declarative import declarative_base

Engine=create_engine('sqlite:///employee.sqlite')
BASE=declarative_base()

class Employee(BASE):

    __tablename__='employee'
    eid=Column(Integer,primary_key=True)
    name=Column(String(200))
    sal=Column(Integer)

    def __init__(self,eid,name,sal):
        self.eid=eid
        self.name=name
        self.sal=sal


BASE.metadata.create_all(Engine)

