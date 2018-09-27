#-*- coding:utf-8 -*-
from django.conf.urls import url
from noticeApp import views

# noticeApp/urls.py

urlpatterns = [
    url('^$', views.HomePageView.as_view(), name='notice' )
]