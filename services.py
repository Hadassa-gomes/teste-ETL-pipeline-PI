from .repositories import SensorRepository
from .utils.cleaning import clean_reading


class SensorService:
    def __init__(self, repository: SensorRepository):
        """
        Camada de serviço responsável por processar leituras de sensores:
        validação, limpeza, enriquecimento e persistência no banco.
        """
        self._repo = repository

    async def process_and_store(self, raw: dict) -> str:
        """
        Executa o fluxo ETL para uma leitura bruta:
        1. Valida e limpa valores.
        2. Enriquece com dados derivados.
        3. Armazena no MongoDB.
        """

        # === Etapa 1: Limpeza e enriquecimento ===
        cleaned = clean_reading(raw.get("temperature"), raw.get("humidity"))

        # === Etapa 2: Montagem do documento final ===
        doc = {
            "device_id": raw.get("device_id"),
            **cleaned,  # campos limpos/enriquecidos
            "raw": {
                "temperature": raw.get("temperature"),
                "humidity": raw.get("humidity"),
            },
        }

        # === Etapa 3: Armazenamento ===
        inserted_id = await self._repo.insert_reading(doc)
        return inserted_id
