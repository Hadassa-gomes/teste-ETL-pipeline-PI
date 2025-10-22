from typing import Dict, List, Any
from .db import init_db, mongo_provider
from .config import settings


class SensorRepository:
    def __init__(self, db_provider=None):
        """
        Repositório responsável por operações de leitura e escrita no MongoDB.
        Permite injeção de um provedor de banco (útil para testes unitários).
        """
        # Injeção de dependência para facilitar testes
        self._provider = db_provider or init_db()
        self._db = self._provider.get_db(settings.mongodb_db)
        self._col = self._db[settings.collection_name]

    async def insert_reading(self, doc: Dict[str, Any]) -> str:
        """Insere uma leitura de sensor no MongoDB e retorna o ID do documento."""
        result = await self._col.insert_one(doc)
        return str(result.inserted_id)

    async def find_recent(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Retorna as leituras mais recentes, ordenadas por 'recorded_at'."""
        cursor = self._col.find().sort("recorded_at", -1).limit(limit)
        return [doc async for doc in cursor]
