from pydantic import BaseSettings


class Settings(BaseSettings):
    mongodb_uri: str
    mongodb_db: str = "mydb"
    collection_name: str = "sensor_readings"
    api_port: int = 8000
    trusted_api_key: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
