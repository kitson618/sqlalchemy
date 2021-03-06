from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, Sequence, and_, or_, text, func
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

# count number of rows of result set by .count()
result_count = session.query(User).filter(User.name.like('%ed')).count()
print(result_count)

""" 
    Expected Result: 
    2
""" 

# count number of rows of result set by func.count()
result = session.query(func.count(User.name), User.name).group_by(User.name).all()
print(result)

""" 
    Expected Result: 
    [(1, u'ed'), (1, u'fred'), (1, u'mary'), (1, u'wendy')]
""" 

# to achieve simple SELECT count(*) FROM table
result = session.query(func.count('*')).select_from(User).scalar()
print(result)

""" 
    Expected Result: 
    4
""" 

# select_from() can be removed if we express the count in terms of the User primary key directly
result = session.query(func.count(User.id)).scalar()
print(result)

""" 
    Expected Result: 
    4
""" 
