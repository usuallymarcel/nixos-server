from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn

class Settings(BaseSettings):
    database_url: PostgresDsn

    model_config = SettingsConfigDict(
        env_file="../../.env",
        case_sensitive=False,
        extra="ignore",
    )

settings = Settings()
