from django.conf.urls import url
from .views import *
from post.views import CommentView,PostCommentView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', BlogList.as_view(),name="allblogs"),
    url(r'^blog/(?P<pk>\d+)/$', BlogView.as_view(),name="oneblog"),
    url(r'^blog/(?P<pk>\d+)/edit/$', EditBlog.as_view(),name="editblog"),
    url(r'^create/$', login_required(AddBlog.as_view()),name="createblog"),
    url(r'^post/(?P<pk>\d+)/$', CommentView.as_view(), name="post_page"),
    url(r'^post/(?P<pk>\d+)/like$', likepost, name="likepost"),
    url(r'^post/(?P<pk>\d+)/countlike$', countlikes, name="countlikes"),
    url(r'^post/(?P<pk>\d+)/comments/$', PostCommentView.as_view(), name="comments"),
    url(r'^blog/(?P<pk>\d+)/edit/post/$', EditPost.as_view(), name="editpost"),
    url(r'^addpost/$', login_required(AddPost.as_view()), name="createpost"),
    url(r'^addpostmodal/$', login_required(CreatePost.as_view()), name="addpostmodal"),
    url(r'^(?P<pk>\d+)/addpost/$', login_required(AddPostFromBlog.as_view()), name="createpostfromblog"),
]
