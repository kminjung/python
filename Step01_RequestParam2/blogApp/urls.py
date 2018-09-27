#-*- coding:utf-8 -*-
from django.conf.urls import url
from blogApp import views

# blogApp/urls.py

urlpatterns = [
    url(r'^$', views.BlogListView.as_view(), name='blog_home'),
    url(r'new/$', views.BlogCreateView.as_view(), name='blog_new'),
]