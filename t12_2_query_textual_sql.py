from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, Sequence, and_, or_, text
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

# using sql expression 1, from_statement(): Execute the given SELECT statement and return results.
query = session.query(User).from_statement(text("SELECT * FROM users where name=:name")).params(name='ed').all()
print(query)

""" 
    Expected Result: 
    [<User(name='ed', fullname='Ed Jones', password='edspassword')>]
""" 

# using sql expression 2
stmt = text("SELECT name, id, fullname, password FROM users where name=:name")
stmt = stmt.columns(User.name, User.id, User.fullname, User.password)
query = session.query(User).from_statement(stmt).params(name='ed').all()
print(query)

""" 
    Expected Result: 
    [<User(name='ed', fullname='Ed Jones', password='edspassword')>]
""" 

# using sql expression 3
stmt = text("SELECT name, id FROM users where name=:name")
stmt = stmt.columns(User.name, User.id)
query = session.query(User.id, User.name).from_statement(stmt).params(name='ed').all()
print(query)

""" 
    Expected Result: 
    [(1, 'ed')]
""" 
