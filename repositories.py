from .db import init_db, mongo_provider
from .config import settings
from typing import Dict


class SensorRepository:
def __init__(self, db_provider=None):
# injeção para facilitar testes
self._provider = db_provider or init_db()
self._db = self._provider.get_db(settings.mongodb_db)
self._col = self._db[settings.collection_name]


async def insert_reading(self, doc: Dict) -> str:
result = await self._col.insert_one(doc)
return str(result.inserted_id)


async def find_recent(self, limit: int = 100):
cursor = self._col.find().sort("recorded_at", -1).limit(limit)
return [doc async for doc in cursor]