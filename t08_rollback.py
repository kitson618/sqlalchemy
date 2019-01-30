ed_user.name = 'Edwardo'

fake_user = User(name='fakeuser', fullname='Invalid', password='12345')
session.add(fake_user)

session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()