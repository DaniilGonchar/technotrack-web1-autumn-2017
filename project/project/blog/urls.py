from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^$', BlogList.as_view(), name='blogspage'),
    url(r'^(?P<myid>\d+)$', posts_list, name='blogsview'),
    url(r'^(?P<myidd>\d+)/(?P<myid>\d+)$', post_page, name='onepost'),
    url(r'^(?P<myidd>\d+)/(?P<pk>\d+)/edit/$', Post_Edit.as_view(), name='post_edit'),
    url(r'^(?P<myidd>\d+)/(?P<pk>\d+)/edit_comment/$', Comment_Edit.as_view(), name='comment_edit'),

    url(r'^new/$', login_required(New_Post.as_view()), name="post_creation"),

]
