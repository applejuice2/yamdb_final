from django.db.models import Avg
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, permissions, viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action, permission_classes
from rest_framework.pagination import PageNumberPagination

from api_yamdb.settings import EMAIL_HOST_USER
from reviews.models import (Categories, Genre, Review,
                            Title, User, ROLES)
from .filters import TitleFilter
from .mixins import CreateListDestroyGenreCategoryBaseViewSet
from .permissions import IsAdmin, IsAdminOrReadOnly
from .permissions import IsAdmin_Moderator_AuthorOrReadOnly
from .serializers import (CategorySerializer, GenreSerializer,
                          TitleListSerializer, TitleCreateSerializer)
from .serializers import ReviewSerializer, CommentSerializer, UserSerializer
from .serializers import SignUpSerializer, ActivateAccountSerializer
from .tokens import account_activation_token


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def create_user(request):
    serializer = SignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    email = serializer.validated_data.get('email').lower()
    try:
        user, _ = User.objects.get_or_create(username=username,
                                             email=email,
                                             is_active=False)
    except IntegrityError:
        if User.objects.filter(username=username,
                               email=email,
                               is_active=True).exists():
            return Response(
                {'error': 'Вы уже активировали ваш аккаунт!'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if User.objects.filter(username=username).exists():
            return Response(
                {'username': f'Username {username} уже занят!'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if User.objects.filter(email=email).exists():
            return Response(
                {'email': f'Email {email} уже занят!'},
                status=status.HTTP_400_BAD_REQUEST
            )
    user.is_active = False
    user.save()
    token = account_activation_token.make_token(user)
    template = render_to_string('api/email_template.html',
                                {'username': username,
                                    'token': token, })
    email = EmailMessage(
        'Код подтверждения для YaMDb!',
        template,
        EMAIL_HOST_USER,
        [email],
    )
    email.send()
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def activate_account(request):
    serializer = ActivateAccountSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    token = serializer.validated_data.get('confirmation_code')
    user = get_object_or_404(User, username=username)
    if account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        refresh = RefreshToken.for_user(user)
        return Response({'token': str(refresh.access_token)},
                        status=status.HTTP_200_OK)
    return Response(
        {'token': f'Токен {token} неверный!'},
        status=status.HTTP_400_BAD_REQUEST
    )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    permission_classes = (IsAdmin,)
    lookup_field = ('username')
    pagination_class = PageNumberPagination

    @action(methods=['get', 'patch', ],
            detail=False,
            url_path='me',
            permission_classes=[permissions.IsAuthenticated], )
    def user_information(self, request):
        if request.method == 'GET':
            user = get_object_or_404(User, username=request.user.username)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        serializer = UserSerializer(request.user, data=request.data,
                                    partial=True)
        serializer.is_valid(raise_exception=True)
        if (request.user.is_user
                and serializer.initial_data.get('role')):
            return Response({'role': ROLES[0][0]},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data,
                        status=status.HTTP_200_OK)


class CategoryViewSet(CreateListDestroyGenreCategoryBaseViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(CreateListDestroyGenreCategoryBaseViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('reviews__score'))
    filter_backends = (DjangoFilterBackend,)
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = PageNumberPagination
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return TitleCreateSerializer
        return TitleListSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAdmin_Moderator_AuthorOrReadOnly,)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs['title_id'])
        return title.reviews.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            title=get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAdmin_Moderator_AuthorOrReadOnly,)

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            pk=self.kwargs['review_id'],
            title__id=self.kwargs['title_id']
        )
        return review.comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            review=get_object_or_404(
                Review,
                pk=self.kwargs.get('review_id'),
                title__id=self.kwargs.get('title_id')
            )
        )
