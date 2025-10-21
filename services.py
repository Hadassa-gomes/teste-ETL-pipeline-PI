from .repositories import SensorRepository
from .utils.cleaning import clean_reading


class SensorService:
def __init__(self, repository: SensorRepository):
self._repo = repository


async def process_and_store(self, raw: dict) -> str:
# Lógica ETL: valida -> limpa -> enriquece -> armazena
cleaned = clean_reading(raw.get("temperature"), raw.get("humidity"))


# juntar metadados
doc = {
"device_id": raw.get("device_id"),
**cleaned,
"raw": {"temperature": raw.get("temperature"), "humidity": raw.get("humidity")},
}


inserted_id = await self._repo.insert_reading(doc)
return inserted_id