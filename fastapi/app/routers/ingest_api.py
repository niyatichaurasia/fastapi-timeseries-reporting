from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.core.deps import get_db
from app.models.metric import Metric
from app.models.ingest_request import MetricIngestRequest

router = APIRouter(prefix="/api", tags=["API Ingestion"])


@router.post("/ingest")
def ingest_metric(data: MetricIngestRequest, db: Session = Depends(get_db)):
    
    # Convert time string to datetime object
    try:
        timestamp = datetime.fromisoformat(data.time)
    except:
        raise HTTPException(status_code=400, detail="Invalid time format")

    # Create Metric record
    record = Metric(
        time=timestamp,
        ava_id=data.ava_id,
        metric_name=data.metric_name,
        value=data.value,
        unit=data.unit,
        extra_data={"description": data.description} if data.description else {}
    )

    db.add(record)
    db.commit()

    return {"status": "success", "message": "Metric ingested"}
