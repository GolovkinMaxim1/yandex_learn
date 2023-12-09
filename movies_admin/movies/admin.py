from django.contrib import admin
from .models import Genre, FilmWork, GenreFilmWork, Person, PersonFilmWork


class GenreFilmWorkInline(admin.TabularInline):
    model = GenreFilmWork
    extra = 1


class PersonFilmWorkInline(admin.TabularInline):
    model = PersonFilmWork
    extra = 1


@admin.register(FilmWork)
class FilmWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'creation_date', 'rating',)
    list_filter = ('creation_date', 'type',)
    search_fields = ('title', 'description', 'id')
    inlines = GenreFilmWorkInline, PersonFilmWorkInline

    def get_inline_instances(self, request, obj=None):
        """
        Связи между кинопроизведениями, жанрами и персонами заводятся на странице редактирования кинопроизведения.
        """
        if obj:
            return super().get_inline_instances(request, obj)
        else:
            return []


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created',)

    list_filter = ('name',)

    search_fields = ('name', 'description', 'id')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'created',)

    list_filter = ('full_name',)

    search_fields = ('name', 'id')
