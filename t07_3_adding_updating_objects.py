from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, Sequence
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# configure Session class with desired options
Session = sessionmaker()

# later, we create the engine
engine = create_engine('sqlite:///:memory:', echo=False)

# associate it with our custom Session class
Session.configure(bind=engine)

# work with the session
session = Session()

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

ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
session.add(ed_user)

# add the user object for wendy, mary, fred to the database session
# to be completed

# write changes to the database    
# to be completed

# update the password for ed_user to 'f8s7ccs'
# to be completed

# print out the first row of User Table with name 'ed'
# to be completed
