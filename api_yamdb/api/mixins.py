from rest_framework import filters, mixins, viewsets, serializers

from .permissions import IsAdminOrReadOnly


class CreateListDestroyGenreCategoryBaseViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'


class UsernameSerializer(serializers.Serializer):
    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                f'Измените ваш username. Он не должен быть {value}')
        return value
