# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length=255)
    text = models.TextField()
    createdata = models.DateTimeField(auto_now_add=True)
    changedata = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blog = models.ForeignKey('blog.Blog', related_name='posts')

    def __str__(self):
        return u'{} ({}) {}'.format(self.postname, self.author, self.text)


class Blog(models.Model):
    name = models.CharField(max_length=255)
    createdata = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name




