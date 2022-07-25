from django.shortcuts import get_object_or_404
from rest_framework import serializers

from reviews.models import (Categories, Genre,
                            Title, ROLES, Comment,
                            Review, User)
from reviews.validators import MinMaxYearValueValidators
from .mixins import UsernameSerializer


class SignUpSerializer(UsernameSerializer):
    username = serializers.RegexField(regex=r'^[\w.@+-]+\Z', max_length=150)
    email = serializers.EmailField(max_length=254)


class ActivateAccountSerializer(serializers.Serializer):
    username = serializers.RegexField(regex=r'^[\w.@+-]+\Z', max_length=150)
    confirmation_code = serializers.CharField(max_length=254)


class UserSerializer(UsernameSerializer, serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=ROLES, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Categories


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleListSerializer(serializers.ModelSerializer):
    """Получаем список произведений"""
    rating = serializers.IntegerField(read_only=True)
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'rating', 'description',
            'genre', 'category'
        )
        read_only_fields = ('name', 'year', 'description',)


class TitleCreateSerializer(serializers.ModelSerializer):
    """
    Создание произведений
    """
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all()
    )
    genre = serializers.SlugRelatedField(
        many=True,
        slug_field='slug',
        queryset=Genre.objects.all()
    )
    # Общий валидатор для модели и сериализатора
    year = serializers.IntegerField(validators=[MinMaxYearValueValidators()])

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    title = serializers.HiddenField(default=None)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['pub_date']

    def validate_score(self, value):
        if not (1 <= value <= 10):
            raise serializers.ValidationError('Проставьте оценку от 1 до 10')
        return value

    def validate(self, data):
        if self.context.get('request').method != 'POST':
            return data
        title = get_object_or_404(
            Title,
            pk=self.context['view'].kwargs['title_id']
        )
        author = self.context.get('request').user
        if Review.objects.filter(
                author=author,
                title=title).exists():
            raise serializers.ValidationError(
                'Вы уже оставляли отзыв к данному произведению!')
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    review = serializers.HiddenField(default=None)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['pub_date']
