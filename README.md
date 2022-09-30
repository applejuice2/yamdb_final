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
[![YandexCloud](https://img.shields.io/badge/-Yandex%20Cloud-464646?style=flat&logo=data:image/png;base64,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&logoColor=FFFFFF&color=00B2FF)](http://cloud.yandex.ru) 
  
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

1. Сделайте форк репозитория и клонируйте его на ваш компьютер.


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
