from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#create sql engine and session
engine = create_engine('sqlite:///sqlite.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()