from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

from app.core.config import settings

engine = create_engine(settings.DVDTHEQUE_DATABASE_URL,
                       connect_args={
                           "options": f"-csearch_path={settings.DVDTHEQUE_SCHEMA_NAME}"
                       }
                       , echo=settings.DEBUG)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator[Session, None, None]:
    """Dependency for getting database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()