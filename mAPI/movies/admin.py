#!/usr/bin/env python
# coding: utf-8

from django.contrib import admin

from .models import Movie

admin.site.register(Movie, admin.ModelAdmin)
