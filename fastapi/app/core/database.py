from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DB_HOST=os.getenv("DATABASE_HOST", "timescaledb_container")
DB_PORT=os.getenv("DATABASE_PORT","5432")
DB_USER=os.getenv("DATABASE_USER","postgres")
DB_PASS=os.getenv("DATABASE_PASSWORD","postgres")
DB_NAME=os.getenv("DATABASE_NAME","ava_db")

DATABASE_URL=f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine=create_engine(DATABASE_URL)
Sessionlocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)