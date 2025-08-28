
# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///real_estate.db"

engine = create_engine(DATABASE_URL, echo=True)  # echo=True shows SQL logs
Session = sessionmaker(bind=engine)

Base = declarative_base()

def init_db():
    """Create database tables based on models."""
    from models import Property, Client, Transaction  # Import here to avoid circular import
    Base.metadata.create_all(bind=engine)
