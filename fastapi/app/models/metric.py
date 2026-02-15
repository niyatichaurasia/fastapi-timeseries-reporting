from sqlalchemy import Column, String, Float, DateTime, JSON
from sqlalchemy.orm import declarative_base

# Base class for SQLAlchemy models
Base = declarative_base()

class Metric(Base):
    __tablename__ = "metrics"

    # Composite Primary Keys 
    time = Column(DateTime, primary_key=True)
    ava_id = Column(String, primary_key=True)
    metric_name = Column(String, primary_key=True)

    # Additional columns for KPI data
    value = Column(Float)
    unit = Column(String)
    extra_data = Column(JSON)  # JSON field for optional extra data
