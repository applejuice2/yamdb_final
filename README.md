![yamdb](https://i.postimg.cc/WzwqvT6y/Snimok-ekrana-2022-07-19-v-023803-transformed.jpg) 


![example workflow](https://github.com/applejuice2/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)  
  
Проект **YaMDb** собирает **отзывы (Review)** пользователей на **произведения (Titles)**. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список **категорий (Category)** может расширяться администратором (например, можно добавить категорию «Изобразительное искусство», «Ювелирка»).

Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

В каждой категории есть **произведения**: книги, фильмы или музыка. Произведению может быть присвоен **жанр (Genre)** из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).

Более подробную информацию вы сможете найти по ссылке - [http://localhost:8000/redoc/](http://localhost/redoc/)

## Основные технологии, используемые в проекте


- [Python](https://www.python.org)
- [Django Rest Framework](https://www.django-rest-framework.org)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [PostgreSQL](https://www.postgresql.org)
- [Docker](https://www.docker.com/#)
- [Nginx](https://nginx.org/ru/)
- [Gunicorn](https://gunicorn.org)


## Как запустить проект:

Клонируйте репозиторий:

```sh
git clone https://github.com/applejuice2/infra_sp2
```

В директории infra/ создайте и заполните env-файл:

```sh
SECRET_KEY=****
DB_ENGINE=django.db.backends.postgresql
DB_NAME=****
POSTGRES_USER=****
POSTGRES_PASSWORD=****
DB_HOST=db
DB_PORT=5432
MAIL=****
PASSWORD=****
```

Запуститите приложения в контейнерах.

Соберите контейнеры и запустите их::

```sh
docker-compose up -d --build
```

Выполните миграции:

```sh
docker-compose exec web python manage.py migrate
```

Создайте суперпользователя:

```sh
docker-compose exec web python manage.py createsuperuser
```

Подключите статику:

```sh
docker-compose exec web python manage.py collectstatic --no-input
```

Для заполнения базы данными необходимо выполнить следующую команду:

```sh
docker-compose exec web python manage.py loaddata fixtures.json
```


## Некоторые примеры запросов к API:
1. Регистрация нового пользователя:

Request (POST-запрос):
```sh
http://127.0.0.1:8000/api/v1/auth/signup/
```

```sh
{

    "email": "string",
    "username": "string"

}
```

Response:
```sh
{

    "email": "string",
    "username": "string"

}
```

2. Получение Токена:

Request (POST-запрос):
```sh
http://127.0.0.1:8000/api/v1/auth/token/
```

```sh
{

    "username": "string",
    "confirmation_code": "string"

}
```

Response:
```sh
{

    "token": "string"

}
```

## Примеры запросов

1. Просмотреть список всех произведений:

Request (GET-запрос):
```sh
http://127.0.0.1:8000/api/v1/titles/
```

Response:
```sh
[

{

    "count": 0,
    "next": "string",
    "previous": "string",
    "results": 

[

{

    "id": 0,
    "name": "string",
    "year": 0,
    "rating": 0,
    "description": "string",
    "genre": 

[

    {}

],
"category": 

                {
                    "name": "string",
                    "slug": "string"
                }
            }
        ]
    }

]
```


2. Добавить отзыв к произведению

Request (POST-запрос):
```sh
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
```

```sh
{

    "text": "string",
    "score": 1

}
```

Response:
```sh
{

    "id": 0,
    "text": "string",
    "author": "string",
    "score": 1,
    "pub_date": "2019-08-24T14:15:22Z"

}
```

3. Изменить данные своей учётной записи:

Request (PATCH-запрос):
```sh
http://127.0.0.1:8000/api/v1/users/me/
```

```sh
{

    "username": "string",
    "email": "user@example.com",
    "first_name": "string",
    "last_name": "string",
    "bio": "string"

}
```

Response:
```sh
{

    "username": "string",
    "email": "user@example.com",
    "first_name": "string",
    "last_name": "string",
    "bio": "string",
    "role": "user"

}
```

## Лицензия
![img](https://img.shields.io/badge/license-MIT-brightgreen)

## Авторы проекта:
- [Влад Иванов](https://github.com/applejuice2/)
- [Алексей Ананченко](https://github.com/AlexeyAnanchenko/)
- [Роман Швидкий](https://github.gitop.top/FLI84/)