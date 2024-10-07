from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

# Database path from env vars
DB_URL = os.getenv('DATABASE_URL_DEV')

# Set up the database engine - responsible for SQL queries, connections, and communication with the database.
engine = create_engine(DB_URL)

# A new session factory bound to the database engine.
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Create a base class for model declarations (table representations).
# Table models will inherit from this class
Base = declarative_base()


# define a generator function that provides a session to interact with the database
def get_db():
    # The session will be provided to whatever calls this function as a dependency
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
