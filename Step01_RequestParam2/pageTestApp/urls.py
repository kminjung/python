#-*- coding:utf-8 -*-
from django.conf.urls import url
from pageTestApp import views

# pageTestApp/urls.py

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(),\
         name='home'),
    url(r'^about/$', views.AboutPageView.as_view(),\
         name='about'),
    url(r'^contact/$', views.ContactPageView.as_view(),\
         name='contact'),
    
]