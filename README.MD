API сервис для создания вопросов и ответов, реализованный с использованием FastAPI и PostgreSQL.  
Позволяет:

- Создавать вопросы.
- Добавлять ответы к вопросам.
- Получать список вопросов и их ответы.
- Удалять вопросы и каскадно удалять связанные ответы.
- Получать и удалять отдельные ответы.

---

## Стек

- Python 3.13
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Docker / Docker Compose
- pytest (для тестов)
---

## Структура проекта

```text
project/
├─ app/                     # Основной код приложения
│  ├─ __init__.py
│  ├─ main.py               # Точка входа приложения
│  ├─ core/                 # Настройки и конфигурация
│  │  └─ config.py          # Настройки (DATABASE_URL, PORT и т.д.)
│  ├─ db/                   # Инициализация БД и сессии
│  │  ├─ base.py            # Общие декларации моделей
│  │  └─ session.py         # Создание SQLAlchemy сессии
│  ├─ models.py             # ORM модели
│  ├─ schemas.py            # Pydantic схемы для запросов и ответов
│  ├─ crud.py               # Функции для работы с БД
│  └─ api/                  # Роуты для API
│     ├─ __init__.py
│     ├─ questions.py       # Эндпоинты вопросов
│     └─ answers.py         # Эндпоинты ответов
├─ alembic/                  # Миграции базы данных
│  ├─ env.py
│  ├─ script.py.mako
│  └─ versions/
│     └─ 0001_initial.py    # Первая миграция для создания таблиц
├─ tests/                    # Тесты
│  ├─ conftest.py            # Фикстуры для pytest
│  └─ test_questions_answers.py
├─ docker-compose.yml        # Конфигурация Docker Compose
├─ Dockerfile                # Dockerfile для веб-сервиса
├─ requirements.txt          # Зависимости Python
└─ alembic.ini               # Конфигурация Alembic
```
## Локальная сборка и запуск через Docker

Для локальной сборки проекта достаточно выполнить следующие команды в корневой папке проекта:
 
```bash
docker-compose build
docker-compose up
```
## Тесты

Тесты используют локальную базу данных. Перед запуском тестов убедитесь, что:

1. Контейнер с PostgreSQL запущен (или локальная БД доступна).  
2. Применены миграции (через `alembic upgrade head`).  
3. В `app/core/config.py` `DATABASE_URL` адрес `"postgresql://postgres:postgres@localhost:5432/qa_db"`.

Запуск тестов:

```bash
pytest
```
