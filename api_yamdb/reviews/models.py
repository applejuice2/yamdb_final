from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

from .validators import MinMaxYearValueValidators

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'

ROLES = (
        (USER, USER),
        (MODERATOR, MODERATOR),
        (ADMIN, ADMIN),
)


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Юзернейм',
        help_text=(
            "Обязательное поле. Не более 150 символов."
            "Только буквы, цифры и @/./+/-/_ ."
        ),
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+\Z',
                message='Некоторые символы не поддерживаются',
            ),
        ],
        error_messages={
            "unique": ("Пользователь с таким юзернеймом уже существует"),
        },
    )
    email = models.EmailField(max_length=254,
                              unique=True,
                              verbose_name='Адрес электронной почты')
    first_name = models.CharField(max_length=150,
                                  blank=True,
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=150,
                                 blank=True,
                                 verbose_name='Фамилия')
    bio = models.TextField(blank=True, verbose_name='Биография')
    role = models.CharField(max_length=max([len(i[0]) for i in ROLES]),
                            choices=ROLES,
                            default=USER,
                            verbose_name='Пользовательская роль')

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        swappable = "AUTH_USER_MODEL"
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    @property
    def is_admin(self):
        return (
            self.role == ADMIN or self.is_staff
            or self.is_superuser
        )

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    @property
    def is_user(self):
        return self.role == USER

    def __str__(self):
        return self.username


class Categories(models.Model):
    """
    Категории используемых в произведениях.
    """
    name = models.CharField(max_length=256,
                            verbose_name='Категория',
                            unique=True)
    slug = models.SlugField(max_length=50,
                            unique=True,
                            verbose_name='Уникальный адрес')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    """
    Жанры используемых произведений.
    """
    name = models.CharField(max_length=256,
                            verbose_name='Жанр произведения',
                            unique=True)
    slug = models.SlugField(unique=True,
                            verbose_name='Уникальный адрес',
                            max_length=50)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    """
    Произведения
    """
    name = models.TextField(verbose_name='Имя произведения')
    year = models.IntegerField(validators=[MinMaxYearValueValidators])
    description = models.TextField(verbose_name='Описание группы', blank=True)
    genre = models.ManyToManyField(Genre, through='GenreTitle', blank=True)
    category = models.ForeignKey(Categories,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 related_name='titles',)

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titles} {self.genre}'


class Review(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    text = models.TextField('Текст',)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    score = models.IntegerField('Оценка',)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_review',
            )
        ]
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text[:20]


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )
    text = models.TextField('Текст',)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:20]
