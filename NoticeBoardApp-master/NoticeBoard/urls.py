from django.conf.urls import patterns, include, url

from NoticeBoard import views

urlpatterns = patterns('',
                       url(r'^$',views.index, name='index'),
                       url(r'^list/$', views.list, name='list'),
                       url(r'^(?P<title_req>\w+)/$', views.detail, name='detail'),
                       )