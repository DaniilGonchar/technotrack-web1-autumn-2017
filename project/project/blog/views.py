# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Post
from comments.models import Comment

from django import forms




def post_page (request, myidd=None, myid=None):
    blog = get_object_or_404(Blog.objects, id=myidd)
    post = get_object_or_404(Post.objects, id=myid)

    if (post.blog.id == blog.id):
        return render (request, 'blog/post_page.html', {'post': post})
    else:
        raise Http404


def posts_list (request, myid=None):
    blog = get_object_or_404(Blog.objects, id=myid)
    return render (request, 'blog/posts_list.html', {'blog': blog})


## post page class

class Post_Edit(UpdateView):
    template_name = 'blog/edit_post.html'
    model = Post
    fields = 'postname', 'text'

    def get_queryset(self):
        return super(Post_Edit, self).get_queryset().filter(
            author=self.request.user,
            blog__pk=self.kwargs['myidd']
        )

    def get_success_url(self):
        return reverse('core:mainpg')







class BlogList(ListView):
    template_name = "blog/blogpage.html"
    context_object_name = 'blog'
    model = Blog




class New_Post(CreateView):
    template_name = 'blog/new_post.html'
    model = Post
    fields = 'postname' , 'text' , 'blog'

    def get_success_url(self):
        return reverse('core:mainpg')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog_id = 5 #self.fields.



        return super(New_Post, self).form_valid(form)


class Comment_Edit(UpdateView):
    template_name = 'blog/edit_comment.html'
    model = Comment
    fields = ('text',)

    def get_queryset(self):
        return super(Comment_Edit, self).get_queryset().filter(
            author=self.request.user,
            #blog__pk=self.kwargs['myidd']
        )

    def get_success_url(self):
        return reverse('core:mainpg')





#   class Post_Form(forms.Form):
#     title = forms.CharField
#     text = forms.CharField(widget=forms.Textarea)
#
#     @login_required
#     def new_post(request):
#         if request.method == 'POST':
#             form = Post_Form
#         if form.is_valid():
#             post = Post(title=form.cleaned_data['title'], text = form.cleaned_data['text'])
#             post.author = request.user
#             post.blog_id = request.user.id
#             post.save()
#             return redirect('posts:currentpost', id = post.id)
#         else:
#             form = Post_Form
#             return render( request , 'blog/new_post.html' , {'form':form} )
#
