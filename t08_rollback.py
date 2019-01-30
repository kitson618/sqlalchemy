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

ed_user.name = 'Edwardo'
fake_user = User(name='fakeuser', fullname='Invalid', password='12345')
session.add(fake_user)

#before rollback
updated_user = session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()
print(updated_user)

session.rollback()

print("ed_user.name: " + ed_user.name)
""" 
    Expected result:
    ed
"""

print(fake_user in session)
""" 
    Expected result:
    False
"""

#after rollback
updated_user = session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all()
print(updated_user)
