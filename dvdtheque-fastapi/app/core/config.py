from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DVDTHEQUE_DATABASE_URL: str
    SECRET_KEY: str
    DEBUG: bool = False
    DVDTHEQUE_SCHEMA_NAME: str
    API_V1_PREFIX: str = "/api/v1"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()