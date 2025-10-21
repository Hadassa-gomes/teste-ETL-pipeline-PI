from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime


class SensorRaw(BaseModel):
temperature: float
humidity: float
device_id: Optional[str] = None
created_at: Optional[datetime] = None


@validator("temperature", "humidity")
def not_nan(cls, v):
if v is None:
raise ValueError("valor nulo não permitido")
return v


class SensorClean(SensorRaw):
# campos normalizados/enriquecidos
temperature_celsius: float = Field(...)
humidity_percent: float = Field(...)
recorded_at: datetime = Field(default_factory=datetime.utcnow)