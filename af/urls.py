﻿from django.conf.urls import patterns, url
from af import views

urlpatterns = patterns('',
    url(r'^candidate', views.candidate, name='candidate'),
    url(r'^$', views.index, name='index'),
    url(r'^log/?$', views.log, name='log'),
    url(r'^log/user/(?P<userid>\d+)$', views.userLog, name='userlog'),
    url(r'^log/email/(?P<email>\S+@\S+)$', views.emailLog, name='emaillog'),
)
