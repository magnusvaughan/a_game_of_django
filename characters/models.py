from django.contrib.postgres.fields import ArrayField
from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    is_female = models.BooleanField()
    culture = models.CharField(max_length=200, blank=True)
    titles = ArrayField(models.CharField(max_length=200), null=True, blank=True)
    aliases = ArrayField(models.CharField(max_length=200), null=True, blank=True)
    born = models.CharField(max_length=200, blank=True)
    died = models.CharField(max_length=200, blank=True)
    father = models.CharField(max_length=200, blank=True)
    mother = models.CharField(max_length=200, blank=True)
    spouse = models.CharField(max_length=200, blank=True)
    children = ArrayField(models.CharField(max_length=200), null=True, blank=True)
    allegiances = ArrayField(models.CharField(max_length=200), null=True, blank=True)
    books = ArrayField(models.CharField(max_length=200), null=True, blank=True)
    pov_books = ArrayField(models.CharField(max_length=200), null=True, blank=True)
    played_by = ArrayField(models.CharField(max_length=200), null=True, blank=True)
    tv_series = ArrayField(models.CharField(max_length=200), null=True, blank=True)
