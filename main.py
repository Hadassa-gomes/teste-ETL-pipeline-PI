from fastapi import FastAPI, Depends, HTTPException, Query
from .config import settings
from .repositories import SensorRepository
from .services import SensorService
from .db import init_db
from pydantic import BaseModel


app = FastAPI(title="Sensor ETL API")


# inicializa a conexão com o MongoDB
init_db()


# Pydantic para endpoint
class IncomingReading(BaseModel):
temperature: float
humidity: float
device_id: str | None = None


# dependência simples para injeção
def get_service():
repo = SensorRepository()
return SensorService(repo)


@app.get("/health")
async def health():
return {"status": "ok"}


@app.post("/ingest")
async def ingest(reading: IncomingReading, service: SensorService = Depends(get_service)):
try:
inserted_id = await service.process_and_store(reading.dict())
return {"status": "stored", "id": inserted_id}
except ValueError as e:
raise HTTPException(status_code=422, detail=str(e))
except Exception as e:
raise HTTPException(status_code=500, detail=str(e))