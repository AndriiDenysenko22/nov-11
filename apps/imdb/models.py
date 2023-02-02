from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Movie(models.Model):
    class TitleType(models.TextChoices):
        short = ('Short', _('Short Movie'))
        movie = ('movie', _('Movie'))

    imdb_id = models.CharField(_('Id from IMDB'), primary_key=True, max_length=80)
    title_type = models.CharField(_('Type of the Movie'), max_length=80, choices=TitleType.choices)
    name = models.CharField(_('Name'), max_length=255)
    is_adult = models.BooleanField(_('Is Adult'), default=False)
    year = models.DateField(_('Year'), null=True)
    genres = ArrayField(models.CharField(_('Genres'), max_length=80))


class Person(models.Model):
    # id = models.AutoField(primary_key=True)
    person_id = models.CharField(_('Person_id'), primary_key=True, max_length=80) #####
    imdb_id = models.CharField(_('Id from IMDB'), max_length=80)
    name = models.CharField(_('Name'), max_length=255)
    birth_year = models.DateField(_('Birth Year'), null=True)
    death_year = models.DateField(_('Death Year'), null=True)


class PersonMovie(models.Model):

    person = models.ForeignKey('Person', on_delete=models.PROTECT, default=None,  null=True)
    imdb = models.ForeignKey('Movie', on_delete=models.PROTECT, default=None, null=True)
    order = models.IntegerField(_('Order'))
    category = models.CharField(_('Category'), max_length=80, null=True)
    job = models.CharField(_('Job'), max_length=255, null=True)
    characters = ArrayField(models.CharField(_('Characters'), max_length=255))
