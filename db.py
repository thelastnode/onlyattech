from bkrypt import Password

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, autoincrement = True)
    username = Column(String(32))
    password = Column(String(256))
    email = Column(String(256))
    name = Column(String(256))

    def __init__(self, username, password, email, name):
        self.username = username
        self.password = str(Password.create(password))
        self.email = email
        self.name = name

    def verify_password(self, password):
        return Password(self.password) == password
