#!/usr/bin/env python
# coding: utf-8

from rest_framework.generics import ListCreateAPIView

from .models import Comment
from .serializers import CommentSerializer


class CommentsView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
