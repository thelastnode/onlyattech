from bkrypt import Password
from sqlalchemy import Column, DateTime, Integer, LargeBinary, String, Text
from sqlalchemy import func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

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


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key = True, autoincrement = True)
    submission_time = Column(DateTime, default=func.now())
    category = Column(String(256))
    text = Column(Text)
    photo = Column(LargeBinary)
    original_text = Column(Text)

    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User', backref=backref('addresses', order_by=id))

    approval_status = Column(Integer, default=0)
    approval_time = Column(DateTime)

    def __init__(self, text, category, author):
        if type(author) == User:
            self.author_id = author.id
        else:
            self.author_id = author

        self.text = text
        self.original_text = text
        self.category = category

    def updatePost(self, new_text):
        self.text = new_text


class Vote(Base):
    __tablename__ = 'votes'

    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    time = Column(DateTime, default=func.now())

    def __init__(self, user_id, post_id):
        self.user_id = user_id
        self.post_id = post_id


class Flag(Base):
    __tablename__ = 'flags'

    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    time = Column(DateTime, default=func.now())

    def __init__(self, user_id, post_id):
        self.user_id = user_id
        self.post_id = post_id
