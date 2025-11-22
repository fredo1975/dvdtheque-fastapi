from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
from app.crud.base import CRUDBase
from app.models.film import Film

class CRUDFilm(CRUDBase[Film]):

    def get_with_relations(self, db: Session, id: int) -> Optional[Film]:
        return db.query(Film).filter(Film.id == id).first()


    def search_by_title(self, db: Session, title: str) -> List[Film]:
        return db.query(Film).filter(Film.title.ilike(f"%{title}%")).all()


film_crud = CRUDFilm(Film)
