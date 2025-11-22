from typing import List

from pydantic import ConfigDict
from sqlalchemy import Column, Integer, String, Date, Boolean, Text, ForeignKey, Table
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.schemas.film import FilmBase, GenreBase, GenreResponse


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
    genres = relationship("Genre", secondary="film_genre", back_populates="films")


# 1. Définition de la table de mapping (instance de Table, pas une classe)
film_genre = Table('film_genre', Base.metadata,
    Column('film_id', Integer, ForeignKey('film.id'), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genre.id'), primary_key=True)
)

class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=True)
    films = relationship("Film", secondary="film_genre", back_populates="genres")


"""
class Dvd(Base):
    __tablename__ = "dvd"

    id = Column(Integer, primary_key=True, index=True)
    annee = Column(Integer, nullable=True)
    zone = Column(Integer, nullable=False)
    edition = Column(String(255), nullable=True)
    date_rip = Column(Date, nullable=True)
    format = Column(String(7), nullable=True)
    ripped = Column(Boolean, nullable=False)
    date_sortie = Column(Date, nullable=True)

class Personne(Base):
    __tablename__ = "personne"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255), nullable=False)
    prenom = Column(String(255), nullable=True)
    date_n = Column(Date, nullable=True)
"""