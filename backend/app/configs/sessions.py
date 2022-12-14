from functools import lru_cache
from typing import Generator

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from .settings import get_settings

engine = create_engine(get_settings().DATABASE_URL, pool_pre_ping=True)

@lru_cache
def create_session() -> scoped_session:
    Session = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=engine)
            )
    return Session

def get_session() -> Generator[scoped_session, None, None]:
    Session = create_session()
    try:
        yield Session
    finally:
        Session.remove()

Base = declarative_base()
