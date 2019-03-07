#!/usr/bin/env python
# coding: utf-8

from django.contrib import admin
from django.urls import path

from mAPI.movies import views as movies_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies', movies_views.MoviesView.as_view()),
]
