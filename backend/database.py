import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

from models import Vehicle, Route, FuelLog  

def create_all():
    print(" Connecting to DB...")
    Base.metadata.create_all(bind=engine)
    print(" Tables created")

if __name__ == "__main__":
    create_all()
