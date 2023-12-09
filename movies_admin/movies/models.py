import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_('created'), auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class FilmTypeChoices(models.TextChoices):
    """Названия сетей для перевода"""
    movie = 'movie', 'Кино'
    tv_show = 'tv_show', 'Телепередача'


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField(verbose_name=_('name'), max_length=64)
    description = models.TextField(verbose_name=_('description'), blank=True)

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = _('Жанр')
        verbose_name_plural = _('Жанры')

    def __str__(self):
        return self.name


class FilmWork(UUIDMixin, TimeStampedMixin):
    title = models.CharField(verbose_name=_('title'), max_length=255)
    description = models.TextField(verbose_name=_('description'), blank=True)
    creation_date = models.DateField(verbose_name=_('creation date'), auto_now_add=True)

    rating = models.FloatField(
        verbose_name=_('rating'),
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    type = models.CharField(verbose_name=_('type'), choices=FilmTypeChoices.choices, default=FilmTypeChoices.movie)

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = _('Фильм')
        verbose_name_plural = _('Фильмы')

    def __str__(self):
        return self.title


class GenreFilmWork(UUIDMixin):
    film_work = models.ForeignKey(verbose_name=_('film work'), to=FilmWork, on_delete=models.CASCADE)
    genre = models.ForeignKey(verbose_name=_('genre'), to=Genre, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)

    class Meta:
        verbose_name = _('Жанр фильма')
        verbose_name_plural = _('Жанры фильмов')
        db_table = "content\".\"genre_film_work"

    def __str__(self):
        return self.genre.name


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(verbose_name=_('full name'), max_length=255)

    class Meta:
        verbose_name = _('Человек')
        verbose_name_plural = _('Люди')
        db_table = "content\".\"person"

    def __str__(self):
        return self.full_name


class PersonFilmWork(UUIDMixin):
    person = models.ForeignKey(verbose_name=_('person'), to=Person, on_delete=models.CASCADE)
    film_work = models.ForeignKey(verbose_name=_('film work'), to=FilmWork, on_delete=models.CASCADE)
    role = models.CharField(verbose_name=_('role'), max_length=255, blank=True)
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)

    class Meta:
        verbose_name = _('Человек фильма')
        verbose_name_plural = _('Люди фильма')
        db_table = "content\".\"person_film_work"

    def __str__(self):
        return self.role
