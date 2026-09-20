from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from loguru import logger

from app.services.database import init_db


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        f\"Привет, {message.from_user.first_name}! Я асинхронный бот на aiogram 3.x.\"
        \"\\nИспользуй /help для списка команд.\"
    )


@router.message(Command(\"help\"))
async def cmd_help(message: Message) -> None:
    await message.answer(
        \"📋 <b>Доступные команды:</b>\\n\"
        \"/start — Начать работу\\n\"
        \"/help — Эта справка\\n\"
        \"/echo — Эхо-ответ\\n\"
        \"/stats — Статистика бота\"
    )


@router.message(Command(\"echo\"))
async def cmd_echo(message: Message) -> None:
    text = message.text.replace(\"/echo \", \"\", 1) if \" \" in message.text else \"\"
    if not text:
        await message.answer(\"Напишите что-нибудь после /echo\")
        return
    await message.answer(f\"🔁 Эхо: {text}\")


@router.message(Command(\"stats\"))
async def cmd_stats(message: Message) -> None:
    await message.answer(\"📊 Статистика пока недоступна\")