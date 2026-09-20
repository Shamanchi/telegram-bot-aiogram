from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    bot_token: str
    database_url: str = \"sqlite+aiosqlite:///./bot.db\"
    redis_url: str = \"redis://localhost:6379/0\"
    webhook_url: Optional[str] = None
    log_level: str = \"INFO\"

    class Config:
        env_file = \".env\"
        env_file_encoding = \"utf-8\"
        extra = \"ignore\"


settings = Settings()