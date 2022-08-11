import os
from pathlib import Path
from dotenv import load_dotenv
from functools import lru_cache
from pydantic import BaseSettings, PostgresDsn

dir_path=(Path(__file__)/"..").resolve()
env_path=os.path.join(dir_path,'.env')

load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    databse_url: PostgresDsn

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
