from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Column, Integer, String, Float
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model, SerializerMixin):
    def __init__(self, magnitude=None, location=None, year=None, id=None):
        self.magnitude = magnitude
        self.location = location
        self.year = year
        self.id = id
        
    __tablename__ = 'earthquakes'
    
    id = Column(Integer, primary_key=True)
    magnitude = Column(Float)
    location = Column(String)
    year = Column(Integer)
    
    def __repr__(self):
        return f'<Earthquake {self.id}, {self.magnitude, {self.location}, {self.year}}>'