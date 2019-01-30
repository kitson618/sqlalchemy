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
    User(name='fred', fullname='Fred Flinstone', password='blah')])

# write to database
session.commit()


# query with LIMIT, OFFSET and ORDER BY
for u in session.query(User).order_by(User.id)[1:3]: 
    print(u)

""" 
    Expected result:
    <User(name='wendy', fullname='Wendy Williams', password='foobar')>
    <User(name='mary', fullname='Mary Contrary', password='xxg527')>
"""
    
# query using filter(), using class-level attributes
for name, in session.query(User.name).filter(User.fullname=='Ed Jones'): 
    print(name)
    
""" 
    Expected result:
    ed
"""

# query with filter() twice, which joins criteria using AND
for user in session.query(User).filter(User.name=='ed').filter(User.fullname=='Ed Jones'): 
    print(user)
    
""" 
    Expected result:
    <User(name='ed', fullname='Ed Jones', password='edspassword')>
"""