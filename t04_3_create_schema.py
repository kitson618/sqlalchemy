from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, Sequence

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)

#added with Sequence
class User(Base):
  __tablename__ = 'users'
  
  id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
  name = Column(String(50))
  fullname = Column(String(50))
  password = Column(String(12))

  def __repr__(self):
    return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

Base.metadata.create_all(engine)
print(repr(User.__table__)) 

""" 
    Expected result: 

    SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
    ()
    SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
    ()
    PRAGMA table_info("users")
    ()
    CREATE TABLE users (
            id INTEGER NOT NULL, 
            name VARCHAR, 
            fullname VARCHAR, 
            password VARCHAR, 
            PRIMARY KEY (id)
    )
    ()
    COMMIT
    
    Table('users', MetaData(bind=None),
            Column('id', Integer(), table=<users>, primary_key=True, nullable=False, default=Sequence('user_id_seq', metadata=MetaData(bind=None))),
            Column('name', String(), table=<users>),
            Column('fullname', String(), table=<users>),
            Column('password', String(), table=<users>), schema=None) 
"""
