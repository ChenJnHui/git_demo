from django.urls import re_path
from . import views

app_name = 'uu'

urlpatterns = [
    re_path('^index/$', views.index, name='index'),
    re_path(r'^say/$', views.say),
]