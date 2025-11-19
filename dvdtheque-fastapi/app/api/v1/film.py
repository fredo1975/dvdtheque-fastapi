from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.crud.film import film_crud
from app.schemas.film import FilmResponse

router = APIRouter()

@router.get("/", response_model=List[FilmResponse])
def get_films(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Get all films with pagination"""
    films = film_crud.get_all(db, skip=skip, limit=limit)
    return films

@router.get("/{film_id}", response_model=FilmResponse)
def get_film(film_id: int, db: Session = Depends(get_db)):
    """Get a specific film by ID"""
    film = film_crud.get_with_relations(db, id=film_id)
    if not film:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Film with id {film_id} not found"
        )
    return film

"""
@router.put("/{film_id}", response_model=FilmResponse)
def update_film(film_id: int, film: FilmUpdate, db: Session = Depends(get_db)):
    
    db_film = film_crud.get(db, id=film_id)
    if not db_film:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Film with id {film_id} not found"
        )
    return film_crud.update(db, db_obj=db_film, obj_in=film)
"""

@router.get("/search/", response_model=List[FilmResponse])
def search_films(
    title: str = Query(..., min_length=1),
    db: Session = Depends(get_db)
):
    """Search films by title"""
    return film_crud.search_by_title(db, title=title)