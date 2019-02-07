from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, Sequence
# to be completed 

Base = declarative_base()
# configure Session class with desired options
# to be completed 

# later, we create the engine
engine = create_engine('sqlite:///:memory:', echo=False)

# associate it with our custom Session class
# to be completed 

# create a Session instance
# to be completed 

#added with Sequence
class User(Base):
  __tablename__ = 'users'
  
  id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
  name = Column(String(50))
  fullname = Column(String(50))
  password = Column(String(12))

  def __repr__(self):
    return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

# create the database 
Base.metadata.create_all(engine)