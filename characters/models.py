from django.contrib.postgres.fields import ArrayField
from django.db import models

class Character(models.Model):
    name = models.TextField()
    is_female = models.BooleanField()
    culture = models.CharField(max_length=200)
    titles = ArrayField(models.CharField(max_length=200), blank=True)
    aliases = ArrayField(models.CharField(max_length=200), blank=True)
    born = models.CharField(max_length=200)
    died = models.CharField(max_length=200)
    father = models.CharField(max_length=200)
    mother = models.CharField(max_length=200)
    spouse = models.CharField(max_length=200)
    children = ArrayField(models.CharField(max_length=200), blank=True)
    allegiances = ArrayField(models.CharField(max_length=200), blank=True)
    books = ArrayField(models.CharField(max_length=200), blank=True)
    pov_books = ArrayField(models.CharField(max_length=200), blank=True)
    played_by = ArrayField(models.CharField(max_length=200), blank=True)
    tv_series = ArrayField(models.CharField(max_length=200), blank=True)
