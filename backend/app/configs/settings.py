from functools import lru_cache

from pydantic import BaseSettings, PostgresDsn

class Settings(BaseSettings):
    DATABASE_HOSTNAME: str = ""
    DATABASE_PORT: str = ""
    DATABASE_PASSWORD: str = ""
    DATABASE_NAME: str = ""
    DATABASE_USERNAME: str = ""
    SECRET_KEY: str = ""
    ALGORITHM: str = ""
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 0
    DATABASE_URL: PostgresDsn = PostgresDsn(url="",scheme="")

@lru_cache
def get_settings() -> Settings:
    settings =  Settings()
    return settings
