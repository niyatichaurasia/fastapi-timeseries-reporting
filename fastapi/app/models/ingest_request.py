from pydantic import BaseModel
from typing import Optional

class MetricIngestRequest(BaseModel):
    time: str
    ava_id: str
    metric_name: str
    value: float
    unit: Optional[str] = None
    description: Optional[str] = None
