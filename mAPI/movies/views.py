#!/usr/bin/env python
# coding: utf-8

from django.db import models
import requests
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import MovieSerializer, TopMoviesSerializer


class MoviesView(APIView):

    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # validate if "title" was provided
        title = request.data.get('title')
        if not title:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # ask omdbapi for movie data
        data = self.get_data_from_omdbapi(title)
        # check if response was given
        if data is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        data = self.tweek_omdbapi_response_data(data)
        # validate data
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            # save movie
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_data_from_omdbapi(self, title):
        req = requests.get(
            'http://www.omdbapi.com/',
            params={'apikey': '9c9c223e', 't': title})
        data = req.json()
        if data.get('Response', 'False') == 'False':
            return None
        return data

    def tweek_omdbapi_response_data(self, data):
        data['Runtime'] = data['Runtime'].strip(' min')
        return {k.lower(): v for k, v in data.items()}


class TopMoviesView(ListAPIView):
    # TODO: verify this view.
    serializer_class = TopMoviesSerializer

    def get_queryset(self):
        qs = Movie.objects.all() \
            .annotate(
                total_comments=models.Count('comments'),
                rank=models.Window(
                    expression=models.functions.DenseRank(),
                    order_by=models.F("total_comments").desc()
                )
            )\
            .only('id') \
            .order_by('rank')
        return qs
