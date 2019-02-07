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
#1st commit
session.commit()

# update the name of ed_user to 'Edwardo'
# to be completed

# create a User instance 'fake_user' and add to Database session
# to be completed

# before rollback, get all the record with user name 'Edwardo', 'fakeuser'
# to be completed
print(updated_user)

# session rollback function call
# to be completed

# print out the name for 'ed_user'
# to be completed

""" 
    Expected result:
    ed
"""

# print out the fake_user object from database session
# to be completed

""" 
    Expected result:
    False
"""

# after rollback,get all the record with user name 'ed', 'fakeuser'
# to be completed
print(updated_user)
