from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app import config
from functools import lru_cache
from fastapi import Depends
from typing_extensions import Annotated


# @lru_cache
# def get_settings():
#     return config.Settings()


settings = config.Settings()

CONN_URL = URL.create(
    drivername=settings.drivername,
    username=settings.dbusername,
    password=settings.password,
    host=settings.host,
    database=settings.database,
)

engine = create_engine(CONN_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
