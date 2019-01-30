from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, Sequence

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=False)

#added with Sequence
class User(Base):
  __tablename__ = 'users'
  
  id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
  name = Column(String(50))
  fullname = Column(String(50))
  password = Column(String(12))

  def __repr__(self):
    return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
print(ed_user.name)
print(ed_user.password)
print(str(ed_user.id))

"""
    Expected Result: 
    ed
    edspassword
    None 
"""