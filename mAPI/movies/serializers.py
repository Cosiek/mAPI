#!/usr/bin/env python
# coding: utf-8

from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class TopMoviesSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField(source='id')
    total_comments = serializers.IntegerField()
    rank = serializers.IntegerField(source='id')
