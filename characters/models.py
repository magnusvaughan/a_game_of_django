from django.contrib.postgres.fields import ArrayField
from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=200, null=True)
    is_female = models.BooleanField()
    culture = models.CharField(max_length=200, null=True)
    titles = ArrayField(models.CharField(max_length=200), null=True)
    aliases = ArrayField(models.CharField(max_length=200), null=True)
    born = models.CharField(max_length=200, null=True)
    died = models.CharField(max_length=200, null=True)
    father = models.CharField(max_length=200, null=True)
    mother = models.CharField(max_length=200, null=True)
    spouse = models.CharField(max_length=200, null=True)
    children = ArrayField(models.CharField(max_length=200), null=True)
    allegiances = ArrayField(models.CharField(max_length=200), null=True)
    books = ArrayField(models.CharField(max_length=200), null=True)
    pov_books = ArrayField(models.CharField(max_length=200), null=True)
    played_by = ArrayField(models.CharField(max_length=200), null=True)
    tv_series = ArrayField(models.CharField(max_length=200), null=True)
