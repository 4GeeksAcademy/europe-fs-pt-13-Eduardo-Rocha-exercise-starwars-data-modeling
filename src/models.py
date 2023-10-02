import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
    
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    user_password = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250), nullable=False)

class Login(Base):
    __tablename__ = 'login'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(Integer, ForeignKey('user.username'))
    user_password = Column(Integer, ForeignKey('user.user_password'))
    login = relationship(User)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    name = Column(String(250))
    homeworld = Column(String(250))
    url = Column(String(250))
    description = Column(String(250))
    _id = Column(Integer)
    uid = Column(Integer)
    __v = Column(Integer)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    rotation_orbit = Column(Integer)
    garvity = Column(String(250))
    population = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(Integer)
    created = Column(String(250))
    edited = Column(String(250))
    name = Column(String(250))
    url = Column(String(250))
    description = Column(String(250))
    _id = Column(Integer)
    uid = Column(Integer)
    __v = Column(Integer)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    model = Column(String(250))
    vehicle_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(250))
    films = Column(String(250))
    pilots = Column(String(250))
    edited = Column(String(250))
    name = Column(String(250))
    url = Column(String(250))
    description = Column(String(250))
    _id = Column(Integer)
    uid = Column(Integer)
    __v = Column(Integer)


class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    favorites_planets = Column(String(250), ForeignKey('favorites_planets.id'))
    favorites_characters = Column(String(250), ForeignKey('favorites_characters.id'))
    favorites_vehicles = Column(String(250), ForeignKey('favorites_vehicles.id'))
    favorites = relationship(User)

class Favorites_Planets(Base):
    __tablename__ = 'favorites_planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('favorites.user_id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    favorites_planets = Column(String(250), ForeignKey('favorites_planets.id'))
    favorites_planets = relationship(Favorites)
    favorites_planets = relationship(Planets)

class Favorites_Characters(Base):
    __tablename__ = 'favorites_characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('favorites.user_id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    favorites_characters = Column(String(250), ForeignKey('favorites_characters.id'))
    favorites_characters = relationship(Favorites)
    favorites_characters = relationship(Characters)

class Favorites_Vehicles(Base):
    __tablename__ = 'favorites_vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('favorites.user_id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    favorites_vehicles = Column(String(250), ForeignKey('favorites_vehicles.id'))
    favorites_vehicles = relationship(Favorites)
    favorites_vehicles = relationship(Vehicles)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
