from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, aliased
from sqlalchemy.sql import func

Base = declarative_base()

# configure Session class with desired options
Session = sessionmaker()

# later, we create the engine
engine = create_engine('sqlite:///:memory:', echo=False)

# associate it with our custom Session class
Session.configure(bind=engine)

# work with the session
session = Session()

# User Table
class User(Base):
    __tablename__ = 'users'
  
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))
    addresses = relationship("Address", back_populates='user') #bidirectional relationship

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

# Address Table
class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

# create the database 
Base.metadata.create_all(engine)

# insert data for User & Address 
session.add_all([
    User(name='jack', fullname='Jack Bean', password='gjffdd'),
    User(name='ed', fullname='Ed Jones', password='edspassword'),
    User(name='wendy', fullname='Wendy Williams', password='foobar'),
    User(name='mary', fullname='Mary Contrary', password='xxg527'),
    User(name='fred', fullname='Fred Flinstone', password='blah'),
    Address(email_address='jack@google.com', user_id=1),
    Address(email_address='j25@yahoo.com', user_id=1)])

# write to database
session.commit()

# Using subqueries
stmt = session.query(Address.user_id, func.count('*').\
    label('address_count')).\
    group_by(Address.user_id).subquery()

for u, count in session.query(User, stmt.c.address_count).\
    outerjoin(stmt, User.id==stmt.c.user_id).order_by(User.id):
    print(u, count)

"""
    Expected Result: 
    <User(name='jack', fullname='Jack Bean', password='gjffdd')> 2
    <User(name='ed', fullname='Ed Jones', password='edspassword')> None
    <User(name='wendy', fullname='Wendy Williams', password='foobar')> None
    <User(name='mary', fullname='Mary Contrary', password='xxg527')> None
    <User(name='fred', fullname='Fred Flinstone', password='blah')> None
"""