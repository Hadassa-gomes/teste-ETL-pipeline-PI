from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings


class MongoClientProvider:
def __init__(self, uri: str):
self._client = AsyncIOMotorClient(uri)


@property
def client(self) -> AsyncIOMotorClient:
return self._client


def get_db(self, db_name: str):
return self._client[db_name]


# instancia compartilhada para a aplicação
mongo_provider: MongoClientProvider | None = None


def init_db():
global mongo_provider
if mongo_provider is None:
mongo_provider = MongoClientProvider(settings.mongodb_uri)
return mongo_provider