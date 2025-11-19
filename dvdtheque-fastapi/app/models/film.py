from pydantic import ConfigDict
from sqlalchemy import Column, Integer, String, Date, Boolean, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP

from app.db.base import Base
from app.schemas.film import FilmBase


class Film(Base):
    __tablename__ = "film"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String(255), nullable=False)
    titre_o = Column(String(255), nullable=True)
    homepage = Column(String(255), nullable=True)
    vu = Column(Boolean, nullable=False)
    annee = Column(Integer, nullable=False)
    origine = Column(Integer, nullable=False)
    poster_path = Column(String(255), nullable=True)
    overview = Column(Text, nullable=True)
    runtime = Column(Integer, nullable=True)
    date_sortie = Column(Date, nullable=True)
    date_insertion = Column(Date, nullable=True)
    update_ts = Column(TIMESTAMP, nullable=True)
    vue_date = Column(Date, nullable=True)
    date_sortie_dvd = Column(Date, nullable=True)

    # Foreign keys
    #dvd_id = Column(Integer, ForeignKey("directors.id", ondelete="SET NULL"), nullable=True)
    #tmdb_id = Column(Integer, nullable=True)
    # Relationships
    #films = relationship("Film", back_populates="director")


class FilmResponse(FilmBase):
    id: int
    #director: Optional[DirectorResponse] = None
    #genres: List[GenreResponse] = []

    model_config = ConfigDict(from_attributes=True)
