from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,
from sqlalchemy import 

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  fullname = Column(String)
  password = Column(String)

  def __repr__(self):
    return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

print(Base.metadata.create_all(engine))            

""" 
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
"""