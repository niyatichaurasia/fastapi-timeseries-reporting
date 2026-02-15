from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
import pandas as pd
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.models.metric import Metric
from datetime import datetime

router = APIRouter()


@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):

    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")

    df = pd.read_csv(file.file)

    required_columns = {"time", "ava_id", "metric_name", "value", "unit"}
    if not required_columns.issubset(df.columns):
        raise HTTPException(
            status_code=400,
            detail=f"CSV must contain these columns: {required_columns}"
        )

    records = []
    for _, row in df.iterrows():
        record = Metric(
            time=datetime.fromisoformat(row["time"]),
            ava_id=row["ava_id"],
            metric_name=row["metric_name"],
            value=row["value"],
            unit=row["unit"],
            extra_data={}
        )
        db.add(record)

    db.commit()
    return {"message": f"{len(df)} rows inserted successfully"}
