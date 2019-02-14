from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, Sequence
from sqlalchemy.orm import sessionmaker, aliased

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

session.add_all([
    User(name='ed', fullname='Ed Jones', password='edspassword'),
    User(name='wendy', fullname='Wendy Williams', password='foobar'),
    User(name='mary', fullname='Mary Contrary', password='xxg527'),
    User(name='fred', fullname='Fred Flinstone', password='blah'),
    User(name=None, fullname='TestNull', password='TestPassword')])

# write to database
session.commit()

# query using filter() with IS NULL - using equals for User name
for fullname, in session.query(User.fullname).filter(User.name == None): 
    print(fullname)

""" 
    Expected result:
    TestNull
"""

print('')

# query using filter() with IS NULL - using is_ for User name
for fullname, in session.query(User.fullname).filter(User.name.is_(None)): 
    print(fullname)

""" 
    Expected result:
    TestNull
"""

print('')

# query using filter() with IS NOT NULL - using NOT equal for User name
# to be completed

""" 
    Expected result:
    Ed Jones
    Wendy Williams
    Mary Contrary
    Fred Flinstone
"""

print('')

# query using filter() with IS NOT NULL - using isnot for User name
# to be completed

""" 
    Expected result:
    Ed Jones
    Wendy Williams
    Mary Contrary
    Fred Flinstone
"""
