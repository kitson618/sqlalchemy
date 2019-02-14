from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, Sequence, and_, or_
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
    User(name='fred', fullname='Fred Flinstone', password='blah')])

# write to database
session.commit()

# using all() to return a list
query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
print(query.all())

""" 
    Expected Result: 
    [<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>,
    <User(name='fred', fullname='Fred Flinstone', password='blah')>]
""" 

# using first() to get the first one as scalar  
print(query.first())

""" 
    Expected Result: 
    <User(name='ed', fullname='Ed Jones', password='f8s7ccs')>
""" 
