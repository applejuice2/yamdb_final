# API YaMDb

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
[![YandexCloud](https://img.shields.io/badge/-YandexCloud-464646?style=flat&logo=data:image/png;base64,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&logoColor=FFFFFF&color=00B2FF)](http://cloud.yandex.ru) 
  
### Общая информация
Проект **YaMDb** собирает **отзывы (Review)** пользователей на **произведения (Titles)**. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список **категорий (Category)** может расширяться администратором (например, можно добавить категорию «Изобразительное искусство», «Ювелирка»).

Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

В каждой категории есть **произведения**: книги, фильмы или музыка. Произведению может быть присвоен **жанр (Genre)** из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).

Развёрнутый проект можно посмотреть по ссылке - [http://yamdbv1ceo.sytes.net/](http://yamdbv1ceo.sytes.net/)

### Требования

- Python 3.7+
- Работает на macOS, Windows, Linux

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

### Workflow
- `tests` - Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8) и запуск pytest. Дальнейшие шаги выполнятся только если push был в ветку master или main.
- `build_and_push_to_docker_hub` - Сборка и доставка докер-образов на Docker Hub 
- `deploy` - Автоматический деплой проекта на боевой сервер. Выполняется копирование файлов из репозитория на сервер:
- `send_message` - Отправка уведомления в Telegram

### Подготовка к запуску workflow:

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

### Запуск проекта на сервере:

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


### Некоторые примеры запросов к API:
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
