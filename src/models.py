import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    loginStatus = Column(Boolean, nullable=False)
    registrationDate = Column(Date, nullable=False)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    postId = Column(Integer, primary_key=True)
    userId = Column(Integer,ForeignKey('user.id'))
    caption = Column(String(250), nullable=False)
    image = Column(String(250), nullable=False)
    edit_post = Column(Boolean, nullable=False)
    eliminate_post = Column(Boolean, nullable=False)
    user=relationship(User, back_populates="user")

class Liked(Base):
    __tablename__ = 'liked'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    likeId = Column(Integer, primary_key=True)
    postId = Column(Integer, ForeignKey('post.postId') )
    eliminate_like = Column(Boolean, nullable=False)
    post = relationship(Post, back_populates="post")

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    commentId = Column(Integer, primary_key=True)
    comment = Column(String(250), nullable=False)
    eliminate_like = Column(Boolean, nullable=False)
    userId = Column(Integer, ForeignKey('user.id') )
    postId = Column(Integer, ForeignKey('post.postId'))
    post = relationship(Post, back_populates="post")
    user = relationship(User, back_populates="user")

class Saved(Base):
    __tablename__ = 'saved'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    savedId = Column(Integer, primary_key=True)
    eliminate_save = Column(Boolean, nullable=False)
    userId = Column(Integer, ForeignKey('user.id') )
    postId = Column(Integer, ForeignKey('post.postId'))
    post = relationship(Post, back_populates="post")
    user = relationship(User, back_populates="user")

    
    

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    followerId= Column(Integer, primary_key=True)
    eliminate_follower = Column(Boolean, nullable=False)
    userId = Column(Integer, ForeignKey('user.id') )
    user = relationship(User, back_populates="user")


class Followed(Base):
    __tablename__ = 'followed'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    followerId= Column(Integer, primary_key=True)
    eliminate_followed = Column(Boolean, nullable=False)
    userId = Column(Integer, ForeignKey('user.id') )
    user = relationship(User, back_populates="user")


    



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')