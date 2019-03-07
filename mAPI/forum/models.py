#!/usr/bin/env python
# coding: utf-8

from django.db import models


class Comment(models.Model):
    movie = models.ForeignKey('movies.Movie', related_name='comments',
                              on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return '{movie_id}: {txt}'.format(
            movie_id=self.movie_id,
            txt=self.text[:23] + ('…' if self.text[23:] else ''))
