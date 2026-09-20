import aiosqlite
from loguru import logger

from app.core.config import settings


async def init_db() -> None:
    \"\"\"Initialize database tables.\"\"\"
    async with aiosqlite.connect(settings.database_url.replace(\"sqlite+aiosqlite:///\", \"\")) as db:
        await db.execute(\"\"\"
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER UNIQUE NOT NULL,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        \"\"\")
        await db.execute(\"\"\"
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                text TEXT,
                message_type TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        \"\"\")
        await db.commit()
    logger.info(\"Database initialized\")