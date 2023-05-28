from pydantic import BaseSettings

class Settings(BaseSettings):
    # Other application settings

    DATABASE_URL: str = "sqlite:///./app.db"

settings = Settings()
