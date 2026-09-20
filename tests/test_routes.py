import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from aiogram.types import Message, User, Chat


@pytest.fixture
def mock_message():
    message = AsyncMock(spec=Message)
    message.from_user = User(id=123, is_bot=False, first_name=\"Test\", username=\"testuser\")
    message.chat = Chat(id=123, type=\"private\")
    message.text = \"/start\"
    message.answer = AsyncMock()
    return message


@pytest.fixture
def mock_state():
    state = AsyncMock()
    state.clear = AsyncMock()
    state.get_data = AsyncMock(return_value={})
    return state


@pytest.mark.asyncio
async def test_cmd_start(mock_message, mock_state):
    from app.api.routes import cmd_start
    await cmd_start(mock_message, mock_state)
    mock_state.clear.assert_awaited_once()
    mock_message.answer.assert_awaited_once()
    assert \"Привет, Test\" in mock_message.answer.call_args[0][0]


@pytest.mark.asyncio
async def test_cmd_help(mock_message):
    from app.api.routes import cmd_help
    await cmd_help(mock_message)
    mock_message.answer.assert_awaited_once()
    assert \"Доступные команды\" in mock_message.answer.call_args[0][0]


@pytest.mark.asyncio
async def test_cmd_echo_with_text(mock_message):
    from app.api.routes import cmd_echo
    mock_message.text = \"/echo hello world\"
    await cmd_echo(mock_message)
    mock_message.answer.assert_awaited_once()
    assert \"Эхо: hello world\" in mock_message.answer.call_args[0][0]


@pytest.mark.asyncio
async def test_cmd_echo_without_text(mock_message):
    from app.api.routes import cmd_echo
    mock_message.text = \"/echo\"
    await cmd_echo(mock_message)
    mock_message.answer.assert_awaited_once()
    assert \"Напишите что-нибудь\" in mock_message.answer.call_args[0][0]


@pytest.mark.asyncio
async def test_cmd_stats(mock_message):
    from app.api.routes import cmd_stats
    await cmd_stats(mock_message)
    mock_message.answer.assert_awaited_once()
    assert \"Статистика\" in mock_message.answer.call_args[0][0]