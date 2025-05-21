from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Football Predictor API"
    VERSION: str = "1.0.0"
    ALLOWED_ORIGINS: list = ["*"]
    
    class Config:
        env_file = ".env"

settings = Settings()
