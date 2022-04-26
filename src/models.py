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
    userId = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique = True)
    password = Column(String(250), nullable=False)
    loginStatus = Column(Boolean, nullable=False)
    registrationDate = Column(Date, nullable=False)
   

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey('user.id'))
    favoriteName = Column(String(250))
    favoriteNature = Column(String(250))
    favoriteStatus = Column(Boolean)
    user=relationship(User, back_populates="user")

class Nature(Base):
    __tablename__ = 'nature'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    natureName = Column(String(250))

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    personName = Column(String(250))
    personNature= Column(String(250), ForeignKey("nature.natureName"))
    person = relationship(Nature,  back_populates="nature")
    


class PersonDetail(Base):
    __tablename__ = 'person_detail'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    personName = Column(String(250))
    detailNature = Column(String(250), ForeignKey("person.personNature") )
    hairColor = Column(String(250))
    favorited = Column(Boolean, ForeignKey("favorite.favoriteStatus") )
    personDetail = relationship(Person,  back_populates="person")
    favoriteStatus = relationship(Favorite, back_populates="favorite")


class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    planetName = Column(String(250))
    planetNature= Column(String(250), ForeignKey("nature.natureName"))
    planet = relationship(Nature,  back_populates="nature")

class PlanetDetail(Base):
    __tablename__ = 'planet_detail'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    planetName = Column(String(250))
    detailNature = Column(String(250), ForeignKey("planet.planetNature") )
    population = Column(Integer)
    favorited = Column(Boolean, ForeignKey("favorite.favoriteStatus") )
    planetDetail = relationship(Planet,  back_populates="planet")
    favoriteStatus = relationship(Favorite, back_populates="favorite")

class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    vehicleName = Column(String(250))
    vehicleNature= Column(String(250), ForeignKey("nature.natureName"))
    vehicle = relationship(Nature,  back_populates="nature")

class VehicleDetail(Base):
    __tablename__ = 'vehicle_detail'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    vehicleName = Column(String(250))
    vehicleNature = Column(String(250), ForeignKey("vehicle.vehicleNature") )
    manufacturer = Column(String(250))
    favorited = Column(Boolean, ForeignKey("favorite.favoriteStatus") )
    vehicleDetail = relationship(Vehicle,  back_populates="vehicle")
    favoriteStatus = relationship(Favorite, back_populates="favorite")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')