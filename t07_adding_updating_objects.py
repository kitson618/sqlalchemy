ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')

session.add(ed_user)
print(ed_user is our_user)

session.add_all([
    User(name='wendy', fullname='Wendy Williams', password='foobar'),
    User(name='mary', fullname='Mary Contrary', password='xxg527'),
    User(name='fred', fullname='Fred Flinstone', password='blah')])

ed_user.password = 'f8s7ccs'

session.dirtyIdentitySet([<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>])

session.newIdentitySet([<User(name='wendy', fullname='Wendy Williams', password='foobar')>,
<User(name='mary', fullname='Mary Contrary', password='xxg527')>,
<User(name='fred', fullname='Fred Flinstone', password='blah')>])

session.commit()

print(ed_user.id)