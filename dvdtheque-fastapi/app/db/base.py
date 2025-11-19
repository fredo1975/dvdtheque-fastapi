from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Base class for all database models"""
    pass

# Import all models here to ensure they're registered with SQLAlchemy
from app.models.film import Film
#from app.models.director import Director
#from app.models.genre import Genre