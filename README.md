# Проект random_coffee_bot


Проект random_coffee_bot — это Telegram-бот, который каждый понедельник объединяет активных пользователей в пары и отправляет им приглашение на офлайн- или онлайн-встречу, чтобы вместе выпить кофе или чай. Вторая рассылка, напоминающая о встрече, проводится в четверг. Алгоритм сортировки, используемый ботом, исключает повторение пар и позволяет пользователям каждый раз встречаться с новым собеседником.

Функционал телеграм-бота:
- для пользователя: регистрация, рассылка с именем и контактными данными коллеги (электронная почта), возможность на время отписаться от рассылкии -  не участвовать в распределении пары (в случае отпуска, болезни и тп) 
- для администратора: просмотр списка всех пользователей, возможность удалить пользователя из проекта, добавить пользователя в администраторы, а так же удалить его оттуда, отключение пользователя от рассылки


## Технологии
[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)](https://www.python.org/)
[![aiogram](https://img.shields.io/badge/aiogram-3.4-blue)](https://docs.aiogram.dev/en/latest/)
[![aiosqlite](https://img.shields.io/badge/aiosqlite-blue)](https://pypi.org/project/aiosqlite/)
[![APScheduler](https://img.shields.io/badge/APScheduler-blue)](https://docs-python.ru/packages/modul-apscheduler-python/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-blue)](https://docs.sqlalchemy.org/en/20/)
[![alembic](https://img.shields.io/badge/alembic-blue)](https://alembic.sqlalchemy.org/en/latest/)
[![pydantic](https://img.shields.io/badge/pydantic-blue)](https://pydantic-docs.helpmanual.io/)


## Запуск проекта

Для развертывания проекта в контейнерах необходимо установить docker compose.

Установка docker compose:
```
sudo apt update
sudo apt install curl
curl -fSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
sudo apt-get install docker-compose-plugin
```

Клонировать репозиторий:
```
git clone https://github.com/Tatiana314/random_coffee_bot.git && cd random_coffee_bot
```

Проект использует базу данных PostgreSQL.
В директории random_coffee_bot необходимо создать и заполнить ".env" с переменными окружения.
```
# Переменные для телеграм бота
BOT_TOKEN='<токен вашего бота>'
GEN_ADMIN_ID=телеграмм id главного администратора>

# Переменные для PostgreSQL
POSTGRES_DB=<название базы данных>
POSTGRES_USER=<имя пользователя>
POSTGRES_PASSWORD=<пароль пользователя>
DB_HOST=db
DB_PORT=5432
DATABASE_URL='postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}'
```
Запустите docker compose:
```
docker compose up
```
Применение миграций и запуск приложение осуществляется автоматически.

## Настройки рассылки
Поменять дни и время рассылки можно в bot_app/core/constants.py
```
class MailingInt(IntEnum):
    MAIL_TO_COUPLES_HOUR = 10  - время рассылки для пар (часы)
    MAIL_TO_COUPLES_MIN = 00 - время рассылки для пар (минуты)
    REMIND_MAIL_HOUR = 10  - время рассылки напоминания (часы)
    REMIND_MAIL_MIN = 00  - время рассылки напоминания (минуты)


class MailingStr(str, Enum):
    TRIGGER = 'cron'
    MAIL_TO_COUPLES_DAY = 'mon' - день расслыки для пар (принимает значения от 0 до 6, или mon, tue, wed, thu, fri, sat, sun, можно задать сразу несколько дней)
    REMIND_MAIL_DAY = 'thu' - день рассылки с напоминанием (принимает значения от 0 до 6, или mon, tue, wed, thu, fri, sat, sun,  можно задать сразу несколько дней)
```


## Команда разработки

[Анна Победоносцева](https://github.com/ZebraHr) (тимлид команды)

[Светлана Шатунова](https://github.com/SvShatunova) (разработчик)

[Ольга Скрябина](https://github.com/ibonish) (разработчик)

[Татьяна Мусатова](https://github.com/Tatiana314) (разработчик)

[Никита Пискунов](https://github.com/Nikitkosss) (разработчик)
