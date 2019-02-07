from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  fullname = Column(String)
  password = Column(String)

  def __repr__(self):
    return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

# to be completed

""" 
    Expected result: 
    
    Table('users', MetaData(bind=None),
            Column('id', Integer(), table=<users>, primary_key=True, nullable=False),
            Column('name', String(), table=<users>),
            Column('fullname', String(), table=<users>),
            Column('password', String(), table=<users>), schema=None) 
"""
