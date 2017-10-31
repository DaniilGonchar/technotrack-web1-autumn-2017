# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from .models import Comment

# Create your views here.


# class New_Comment(CreateView):
#     template_name = 'blog/new_comment.html'
#     model = Comment
#     fields = 'text'
    # def get_success_url(self):
    #     return reverse('core:mainpg')
    #
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     form.instance.blog_id = self.request.user.id
    #
    #     return super(New_Post, self).form_valid(form)
    #
