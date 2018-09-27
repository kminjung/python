#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.list import ListView
from blogApp.models import Blog
from django.views.generic.edit import CreateView

# blogApp/views.py

# 새글 추가 폼을 출력하기 위한 클래스 정의 
class BlogCreateView(CreateView):
    model=Blog
    template_name='blog/new.html'
    fields=['title', 'content', 'author']

class BlogListView(ListView):
    model=Blog
    template_name='blog/home.html'
