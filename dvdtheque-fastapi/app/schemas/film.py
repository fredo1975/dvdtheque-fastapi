from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List
from datetime import date, datetime

from sqlalchemy import Boolean


class FilmBase(BaseModel):
    titre: str
    titre_o: Optional[str] = None
    homepage: Optional[str] = None
    vu: bool
    annee: int
    origine: int
    poster_path: Optional[str] = None
    overview: Optional[str] = None
    runtime: Optional[int] = None
    date_sortie: date
    date_insertion: date
    update_ts: Optional[datetime] = None
    vue_date: Optional[date] = None
    date_sortie_dvd: Optional[date] = None



class FilmUpdate(BaseModel):
    titre: Optional[str] = None
    titre_o: Optional[str] = None
    release_date: Optional[date] = None
    duration: Optional[int] = Field(None, gt=0)
    rating: Optional[float] = Field(None, ge=0, le=10)
    description: Optional[str] = None
    poster_url: Optional[str] = None
    director_id: Optional[int] = None
    genre_ids: Optional[List[int]] = None


class FilmResponse(FilmBase):
    id: int
    #director: Optional[DirectorResponse] = None
    #genres: List[GenreResponse] = []

    model_config = ConfigDict(from_attributes=True)