from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, Sequence
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
# an Engine, which the Session will use for connection
engine = create_engine('sqlite:///:memory:', echo=False)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
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

# write changes to the database
session.commit()

our_user = session.query(User).filter_by(name='ed').first()
print(our_user)

""" 
    Expected result:
    <User(name='ed', fullname='Ed Jones', password='edspassword')>
"""

print(ed_user)
""" 
    Expected result:
    <User(name='ed', fullname='Ed Jones', password='edspassword')>
"""

print(ed_user is our_user)
""" 
    Expected result:
    True
"""