import django_filters as filters

from reviews.models import Title


# https://django-filter.readthedocs.io/en/latest/guide/
# rest_framework.html#adding-a-filterset-with-filterset-class
class TitleFilter(filters.FilterSet):
    category = filters.CharFilter(
        field_name='category__slug'
    )
    genre = filters.CharFilter(field_name='genre__slug')
    name = filters.CharFilter(field_name='name', lookup_expr='contains')
    # Год предположительно не надо переопределять, тк условие идет по умолчанию
    year = filters.NumberFilter(field_name='year')

    class Meta:
        model = Title
        fields = ['category', 'genre', 'name', 'year']
