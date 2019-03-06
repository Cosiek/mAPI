from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.PositiveSmallIntegerField()
    runtime = models.PositiveSmallIntegerField(verbose_name="Runtime in minutes")
    genre = models.CharField(max_length=65)
    director = models.CharField(max_length=65)
    country = models.CharField(max_length=65)
