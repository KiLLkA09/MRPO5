from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Buyer(Base):
    __tablename__ = 'buyers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    budget = Column(Float, nullable=False)

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    vin = Column(String, unique=True, nullable=False)
