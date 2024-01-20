# Django_event_organizer
## Создание мероприятий: люди, организации, чат на WebSocket

Документация (доступна после запуска проекта):

http://127.0.0.1/swagger/

http://127.0.0.1/redoc/

Проект упакован в контейнеры Docker для локального запуска.

Добавлены .csv файлы вместе со специальной management-командой для заполнения БД.


### Технологии

Python 3.9, Django 3.2, DRF 3.14, Django Channels, Docker, PostgreSQL 13.0, Redis 5.0.1, Daphne 3.0.0, Gunicorn 21.2, Nginx 1.21

### Запуск проекта локально

Склонируйте репозиторий:

```git clone git@github.com:Faithdev21/django_event_organizer.git```

либо

```git clone https://github.com/Faithdev21/django_event_organizer.git```

Добавьте файл с названием .env в backend/test_project (туда же, где .env.example) и заполните его:

```
SECRET_KEY=django-insecure-r7=j=j2^+d-vx(rm%0wpa7b!r5t#wb#yeffoq2#co*^2(pg2oy
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost,backend
DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

Из директории с docker-compose выполните:

```docker-compose up -d```

Для пересборки образа (в случае обновления содержимого проекта) дополните команду так:

```docker-compose up -d --build```

Примените миграции:

```docker-compose exec backend python manage.py migrate```

Создайте суперюзера:

```docker-compose exec backend python manage.py createsuperuser```

### Тестирование API

Для удобства тестирования можно выполнить команду загрузки тестовых данных в БД:

```docker-compose exec web python manage.py populate_db```

Документация API:

http://127.0.0.1/swagger/

http://127.0.0.1/redoc/

### Автор проекта

Егор Лоскутов

https://github.com/Faithdev21