import os
import secrets
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Settings(BaseSettings):
    admin_api_key: str = os.getenv("ADMIN_API_KEY")
    jwt_access_key: str = os.getenv("JWT_ACCESS_KEY", secrets.token_hex(32))
    jwt_refresh_key: str = os.getenv("JWT_REFRESH_KEY", secrets.token_hex(32))
    jwt_access_expiration: int = timedelta(minutes=15).total_seconds()
    jwt_refresh_expiration: int = timedelta(weeks=3).total_seconds()
    jwt_algorithm: str = "HS256"
    db_host: str = os.getenv("DB_HOST", "localhost")
    db_port: int = int(os.getenv("DB_PORT")) if os.getenv("DB_PORT") else 3306
    db_user: str = os.getenv("DB_USER")
    db_password: str = os.getenv("DB_PASSWORD")
    db_name: str = os.getenv("DB_NAME")
    cors_allow_origins: str = (
        list(map(lambda x: x.strip(), os.getenv("CORS_ALLOW_ORIGINS").split(",")))
        if os.getenv("CORS_ALLOW_ORIGINS")
        else ["*"]
    )


config: Settings = Settings()
