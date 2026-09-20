import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.storage.memory import MemoryStorage
from loguru import logger

from app.core.config import settings
from app.core.logging import logger
from app.services.database import init_db
from app.api.routes import router


async def main() -> None:
    logger.info(\"Starting Telegram bot...\")
    
    # Initialize database
    await init_db()
    
    # Setup storage
    if settings.redis_url and settings.redis_url != \"redis://localhost:6379/0\":
        storage = RedisStorage.from_url(settings.redis_url)
    else:
        storage = MemoryStorage()
    
    # Create bot and dispatcher
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(storage=storage)
    
    # Include routers
    dp.include_router(router)
    
    # Start polling
    if settings.webhook_url:
        logger.info(f\"Starting webhook on {settings.webhook_url}\")
        # Webhook setup would go here
    else:
        logger.info(\"Starting polling...\")
        await dp.start_polling(bot)


if __name__ == \"__main__\":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info(\"Bot stopped\")