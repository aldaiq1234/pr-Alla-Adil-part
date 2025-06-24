from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    fuel_type = Column(String)
    license_plate = Column(String)

class Route(Base):
    __tablename__ = "routes"
    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    start_location = Column(String)
    end_location = Column(String)
    distance_km = Column(Float)
    estimated_time = Column(Float)

class FuelLog(Base):
    __tablename__ = "fuel_logs"
    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    date = Column(Date)
    fuel_used_liters = Column(Float)
    fuel_siphoned_liters = Column(Float)