from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List
from datetime import date, datetime

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
    #dvd_id: Optional[int] = None

class GenreBase(BaseModel):
    name: Optional[str] = None

class PersonneBase(BaseModel):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    date_n: Optional[date] = None
    profile_path: Optional[str] = None

class DvdBase(BaseModel):
    edition: Optional[str] = None
    format: Optional[str] = None
    date_rip: Optional[date] = None
    date_sortie: Optional[date] = None
    annee: Optional[int] = None
    zone: Optional[int] = None
    ripped: Optional[bool] = None

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

class GenreResponse(GenreBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class DvdResponse(DvdBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class PersonneResponse(PersonneBase):
    id: int
    #genres: Optional[List[GenreResponse]] = []

    model_config = ConfigDict(from_attributes=True)

class FilmResponse(FilmBase):
    id: int
    genres: Optional[List[GenreResponse]] = []
    realisateurs: Optional[List[PersonneResponse]] = []
    acteurs: Optional[List[PersonneResponse]] = []
    dvd: Optional[DvdResponse] = None

    model_config = ConfigDict(from_attributes=True)