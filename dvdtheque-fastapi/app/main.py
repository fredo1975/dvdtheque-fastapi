# main.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.film import router as films_router

# FastAPI app
app = FastAPI(title="Dvdtheque API",
description="API for managing films",
              version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(films_router, prefix=f"{settings.API_V1_PREFIX}/films", tags=["film"])
#app.include_router(directors.router, prefix=f"{settings.API_V1_PREFIX}/directors", tags=["directors"])
#app.include_router(genres.router, prefix=f"{settings.API_V1_PREFIX}/genres", tags=["genres"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to Films API",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Routes

"""
@app.get("/")
def read_root():
    return {
        "message": "FastAPI PostgreSQL Application",
        "endpoints": {
            "GET /": "This message",
            "GET /films": "List all films",
            "GET /users/{user_id}": "Get user by ID",
            "POST /users": "Create new user",
            "DELETE /users/{user_id}": "Delete user"
        }
    }

@app.get("/films", response_model=List[FilmResponse])
def get_users(skip: int = 0, db: Session = Depends(get_db)):
    return film_crud.get_films(skip, db)

@app.get("/users/{user_id}", response_model=FilmResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(FilmDB).filter(FilmDB.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users", response_model=FilmResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    existing = db.query(FilmDB).filter(FilmDB.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_user = FilmDB(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(FilmDB).filter(FilmDB.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"message": f"User {user_id} deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)