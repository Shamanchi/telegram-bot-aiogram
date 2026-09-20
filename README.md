# Telegram Bot with aiogram 3.x

**Асинхронный Telegram-бот с FSM, middleware, .env-конфигом**

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
[![aiogram](https://img.shields.io/badge/aiogram-3.13-2CA5E0?logo=telegram)](https://docs.aiogram.dev)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Описание

Полнофункциональный асинхронный Telegram-бот на aiogram 3.x с:
- FSM (Finite State Machine) - управление состояниями диалогов
- Middleware - логирование, валидация, rate limiting
- .env конфигурация - через pydantic-settings
- PostgreSQL/SQLite + Redis - хранение данных и кэш
- Webhook / Polling - два режима запуска
- Docker + Docker Compose - готовый к деплою

---

## Архитектура

`mermaid
graph TD
    A[User] --> B[Telegram API]
    B --> C[aiogram Dispatcher]
    C --> D[Middleware Chain]
    D --> E[Router: Commands]
    D --> F[Router: FSM]
    D --> G[Router: Callbacks]
    E --> H[Services]
    F --> H
    G --> H
    H --> I[(Database)]
    H --> J[(Redis Cache)]
`

---

## Быстрый старт

### Локально
`ash
git clone https://github.com/Shamanchi/telegram-bot-aiogram
cd telegram-bot-aiogram
cp .env.example .env
# Отредактируйте .env - добавьте BOT_TOKEN от @BotFather
docker-compose up -d
# или без Docker:
python -m app.main
`

### Переменные окружения (.env)
| Переменная | Описание | По умолчанию |
|------------|----------|--------------|
| BOT_TOKEN | Токен от @BotFather | обязательно |
| DATABASE_URL | URL БД (SQLite/PostgreSQL) | sqlite+aiosqlite:///./bot.db |
| REDIS_URL | URL Redis для FSM/кэша | redis://localhost:6379/0 |
| WEBHOOK_URL | URL для вебхука (опционально) | - |
| LOG_LEVEL | Уровень логирования | INFO |

---

## Команды бота

| Команда | Описание |
|---------|----------|
| /start | Начать работу, регистрация пользователя |
| /help | Справка по командам |
| /echo <текст> | Эхо-ответ |
| /stats | Статистика (заглушка) |

---

## Тесты

`ash
pytest -v
pytest --cov=app --cov-report=term-missing
pytest -m "not integration"
`

---

## Docker

`ash
docker build -t telegram-bot-aiogram .
docker-compose up -d
docker-compose logs -f bot
`

---

## Структура проекта

`
telegram-bot-aiogram/
├── app/
│   ├── api/
│   │   └── routes.py
│   ├── core/
│   │   ├── config.py
│   │   └── logging.py
│   ├── services/
│   │   └── database.py
│   └── main.py
├── tests/
│   └── test_routes.py
├── .github/workflows/ci.yml
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── pyproject.toml
├── .env.example
└── README.md
`

---

## CI/CD

GitHub Actions workflow:
- Ruff (линтинг)
- MyPy (типизация)
- Pytest (тесты)
- Docker build проверка

---

## Лицензия

MIT - см. LICENSE

---

## Контакты

- GitHub: Shamanchi
- Telegram: @PavelYrevichh
- Email: Lietman46@mail.ru

---

> Источник темы: Каталог портфолио, запись telegram-bot-aiogram