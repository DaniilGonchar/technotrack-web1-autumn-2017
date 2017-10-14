# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey('blog.Post')
    text = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL)