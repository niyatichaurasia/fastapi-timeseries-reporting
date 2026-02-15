from fastapi import FastAPI
from sqlalchemy.exc import OperationalError
import time

from app.core.database import engine
from app.models.metric import Metric, Base   # Import BOTH Base and Metric


# IMPORT THE CSV ROUTER
from app.routers.ingest_csv import router as csv_router
from app.routers.ingest_api import router as api_router

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# REGISTER ROUTER HERE
app.include_router(csv_router)
app.include_router(api_router)

# Run this when the app starts
@app.on_event("startup")
def create_tables():
    attempts = 10
    while attempts > 0:
        try:
            print(">>> TRYING TO CONNECT & CREATE TABLES...")
            Base.metadata.create_all(bind=engine)
            print(">>> TABLES CREATED SUCCESSFULLY <<<")
            return
        except OperationalError as e:
            print("DB not ready yet... retrying...")
            attempts -= 1
            time.sleep(2)
    print(">>> FAILED TO CONNECT TO DB AFTER 10 TRIES <<<")


@app.get("/")
def root():
    return {"message": "Backend is running!"}


@app.get("/health")
def health():
    return {"status": "ok"}
