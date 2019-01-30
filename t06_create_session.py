from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)  # once engine is available

session = Session()