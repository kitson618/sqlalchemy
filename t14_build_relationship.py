from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, Sequence, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

# create the database engine, set echo to True to log tracing
engine = create_engine('sqlite:///:memory:', echo=True)

# User Table
class User(Base):
    __tablename__ = 'users'
  
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

# Address Table
class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    # create relationship with anther table 'User'
    # to be completed

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

# create 'User.addresses', in which referred to as a bidirectional relationship with Table 'Address', order_by Address id
# to be completed

# create the database 
Base.metadata.create_all(engine)
