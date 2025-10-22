from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime


class SensorRaw(BaseModel):
    temperature: float
    humidity: float
    device_id: Optional[str] = None
    created_at: Optional[datetime] = None

    @field_validator("temperature", "humidity")
    @classmethod
    def not_nan(cls, v):
        if v is None:
            raise ValueError("valor nulo não permitido")
        return v


class SensorClean(SensorRaw):
    # Campos normalizados/enriquecidos
    temperature_celsius: float = Field(...)
    humidity_percent: float = Field(...)
    recorded_at: datetime = Field(default_factory=datetime.utcnow)
