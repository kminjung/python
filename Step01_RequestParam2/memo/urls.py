#-*- coding:utf-8 -*-

'''
    memo/urls.py
'''

#-*- coding:utf-8 -*-
from django.conf.urls import url, include
from memo import views

urlpatterns = [
    url(r'^hello/$', views.hello),
    url(r'^list/$', views.list),
]

























