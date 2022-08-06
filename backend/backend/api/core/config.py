from dotenv import load_dotenv
from pathlib import Path
import os

dir_path=(Path(__file__)/"..").resolve()
env_path=os.path.join(dir_path,'.env')

load_dotenv(dotenv_path=env_path)

class Settings():
    APP_TITLE: str = os.getenv("APP_TITLE") or "My API"
    APP_VERSION: str = os.getenv("APP_VERSION") or "0.0.1"
    APP_HOST: str = os.getenv("APP_HOST") or "0.0.0.0"
    APP_PORT: str = os.getenv("APP_PORT") or "8001"


settings = Settings()
