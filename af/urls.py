from django.conf.urls import patterns, url
from af import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^log/?$', views.log, name='log'),
    url(r'^log/user/(?P<userid>\d+)$', views.userLog, name='userlog'),
    url(r'^log/email/(?P<email>\d+)$', views.emailLog, name='emaillog'),
)
