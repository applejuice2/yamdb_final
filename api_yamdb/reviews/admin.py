from django.contrib import admin

from .models import (User, Categories,
                     Genre, Title,
                     Review, Comment)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role')
    list_display_links = ('id', 'role')
    search_fields = ('username',)
    empty_value_display = '-пусто-'


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'slug')
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'slug')
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year',
                    'description', 'category')
    list_display_links = ('id', 'name',
                          'description')
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text',
                    'author', 'score',
                    'pub_date')
    list_display_links = ('id', 'title',
                          'score')
    list_filter = ('title', 'pub_date')
    search_fields = ('title',)
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'review', 'text',
                    'author', 'pub_date')
    list_display_links = ('id',)
    list_filter = ('pub_date',)
    search_fields = ('author',)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
