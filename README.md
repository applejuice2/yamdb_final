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
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=data:image/png;base64,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&logoColor=FFFFFF&color=00B2FF)](https://cloud.yandex.ru/) 
  
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
