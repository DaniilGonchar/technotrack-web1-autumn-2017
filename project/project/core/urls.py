from django.conf.urls import url

from core import views
from core.views import *

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='mainpg'),
    url(r'^new$',views.RegisterFormView.as_view(), name='signup')
]