# YaMDb

![img](https://img.shields.io/badge/license-MIT-brightgreen)
![example workflow](https://github.com/applejuice2/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=FFFFFF&color=00B2FF)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=FFFFFF&color=00B2FF)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-DRF-464646?style=flat&logo=Django%20REST%20Framework&logoColor=FFFFFF&color=00B2FF)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=FFFFFF&color=00B2FF)](https://www.postgresql.org/)
[![JWT](https://img.shields.io/badge/-JWT-464646?style=flat&color=00B2FF)](https://jwt.io/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=FFFFFF&color=00B2FF)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=FFFFFF&color=00B2FF)](https://gunicorn.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=FFFFFF&color=00B2FF)](https://www.docker.com/)
[![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat&logo=Docker&logoColor=FFFFFF&color=00B2FF)](https://www.docker.com/)
[![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=FFFFFF&color=00B2FF)](https://www.docker.com/products/docker-hub)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat&logo=GitHub%20actions&logoColor=FFFFFF&color=00B2FF )](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=Yandex.Cloud&logoColor=FFFFFF&color=00B2FF)](https://cloud.yandex.ru/)
  
  
Проект **YaMDb** собирает **отзывы (Review)** пользователей на **произведения (Titles)**. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список **категорий (Category)** может расширяться администратором (например, можно добавить категорию «Изобразительное искусство», «Ювелирка»).

Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

В каждой категории есть **произведения**: книги, фильмы или музыка. Произведению может быть присвоен **жанр (Genre)** из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).

Развёрнутый проект можно посмотреть по ссылке - [https://yamdbv1ceo.sytes.net/](https://yamdbv1ceo.sytes.net/)

### Ресурсы API YaMDb

- Ресурс `auth`: аутентификация.
- Ресурс `users`: пользователи.
- Ресурс `titles`: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
- Ресурс `categories`: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
- Ресурс `genres`: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- Ресурс `reviews`: отзывы на произведения. Отзыв привязан к определённому произведению.
- Ресурс `comments`: комментарии к отзывам. Комментарий привязан к определённому отзыву.
Каждый ресурс описан в документации Redoc: указаны эндпоинты (адреса, по которым можно сделать запрос), разрешённые типы запросов, права доступа и дополнительные параметры, если это необходимо.

Более подробную информацию вы сможете найти по ссылке - [http://yamdbv1ceo.sytes.net/redoc/](http://yamdbv1ceo.sytes.net/redoc/)


### Пользовательские роли

- **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.
- **Аутентифицированный пользователь** (`user`) — может читать всё, как и Аноним, может публиковать отзывы и ставить оценки произведениям (фильмам/книгам/песенкам), может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.
- **Модератор** (`moderator`) — те же права, что и у Аутентифицированного пользователя, плюс право удалять и редактировать любые отзывы и комментарии.
- **Администратор** (`admin`) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
- **Суперюзер** Django должен всегда обладать правами администратора, пользователя с правами `admin`. Даже если изменить пользовательскую роль суперюзера — это не лишит его прав администратора. Суперюзер — всегда администратор, но администратор — не обязательно суперюзер.

## Workflow
- `tests` - Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8) и запуск pytest. Дальнейшие шаги выполнятся только если push был в ветку master или main.
- `build_and_push_to_docker_hub` - Сборка и доставка докер-образов на Docker Hub 
- `deploy` - Автоматический деплой проекта на боевой сервер. Выполняется копирование файлов из репозитория на сервер:
- `send_message` - Отправка уведомления в Telegram

## Подготовка к запуску workflow:

1. Сделайте форк и репозитория и клонируйте его.


2. Создайте воркфлоу с названием **yamdb_workflow** в репозитории вашего проекта.


3. На github создайте следующие секреты *(Settings - Secrets - Actions secrets)*:

***SECRET_KEY*** -  ваш ключ к защите подписанных данных (указывается в кавычках).

***DB_ENGINE*** - используемая БД (по умолчанию - django.db.backends.postgresql).

***DB_NAME*** - имя созданной БД.

***POSTGRES_USER*** - имя пользователя БД.

***POSTGRES_PASSWORD*** - пароль для пользователя БД.

***DB_HOST*** - localhost (по умолчанию db).

***DB_PORT*** - порт для подключения к БД.

***MAIL*** - почта, с которой будут отправляться письма с кодом для получения токена при регистрации

***MAIL_PASSWORD*** - пароль от почты

***DOCKER_USERNAME*** - username вашего аккаунта Docker Hub

***DOCKER_PASSWORD*** - пароль от вашего Docker Hub аккаунта

***HOST*** - публичный IP адрес машины

***PASSPHRASE*** - если при создании ssh-ключа вы использовали фразу-пароль, то сохраните её в данную переменную  

***SSH-KEY*** - приватный SSH ключ вашего компьютера с доступом к серверу (получить можно командой  cat ~/.ssh/id_rsa)

***TELEGRAM_TO*** - id телеграм-аккаунта, которому будут приходить сообщения с результатом workflow. Узнать свой ID можно у бота *@userinfobot*.

***TELEGRAM_TOKEN*** - токен вашего бота. Получить этот токен можно у бота *@BotFather*.


4. Зайдите в репозиторий на локальной машине и отправьте следующие файлы на сервер:
```sh
scp docker-compose.yaml <username>@<host>/home/<username>/docker-compose.yaml
sudo mkdir nginx
scp default.conf <username>@<host>/home/<username>/nginx/default.conf
```

## Запуск проекта на сервере:

 1. Войдите на удалённый сервер
 
 
 2. Остановите nginx командой:
 ```sh
 sudo systemctl stop nginx
 ```
 3.  Установите Docker на ваш сервер:

 ```sh
 sudo apt install docker.io
  ```
4. Установите Docker-compose на ваш сервер:

```sh
sudo curl -L "https://github.com/docker/compose/releases/download/v2.6.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```

5. Успешность установки Docker-compose можно проверить следующей командой:
```sh
docker-compose --version
```

6. Выполните миграции:

```sh
sudo docker-compose exec web python manage.py migrate
```

7. Создайте суперпользователя:

```sh
sudo docker-compose exec web python manage.py createsuperuser
```

8. Подключите статику:

```sh
sudo docker-compose exec web python manage.py collectstatic --no-input
```

9. Для заполнения базы данными необходимо выполнить следующую команду:

```sh
sudo docker-compose exec web python manage.py loaddata fixtures.json
```


## Некоторые примеры запросов к API:
- Регистрация нового пользователя:
>http://127.0.0.1:8000/api/v1/auth/signup/

*Request (POST-запрос):*
```json
{
    "email": "string",
    "username": "string"
}
```

*Response:*
```json
{
    "email": "string",
    "username": "string"
}
```

- Получение Токена:
>http://127.0.0.1:8000/api/v1/auth/token/

*Request (POST-запрос):*
```json
{
    "username": "string",
    "confirmation_code": "string"
}
```

*Response:*
```json
{
    "token": "string"
}
```

- Добавление отзыва к произведению:
>http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/

*Request (POST-запрос):*
```json
{
    "text": "string",
    "score": 1
}
```

*Response:*
```json
{
    "id": 0,
    "text": "string",
    "author": "string",
    "score": 1,
    "pub_date": "2019-08-24T14:15:22Z"
}
```

- Изменение данных своей учётной записи:
>http://127.0.0.1:8000/api/v1/users/me/

*Request (PATCH-запрос):*
```json
{
    "username": "string",
    "email": "user@example.com",
    "first_name": "string",
    "last_name": "string",
    "bio": "string"
}
```

*Response:*
```json
{
    "username": "string",
    "email": "user@example.com",
    "first_name": "string",
    "last_name": "string",
    "bio": "string",
    "role": "user"
}
```


## Авторы проекта:
- [Влад Иванов](https://github.com/applejuice2/)
- [Алексей Ананченко](https://github.com/AlexeyAnanchenko/)
- [Роман Швидкий](https://github.gitop.top/FLI84/)
