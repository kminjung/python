#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import TemplateView

# pageTestApp/views.py

# 함수 기반이 아닌 클래스 기반으로 views.py 정의하기

class HomePageView(TemplateView):
    # 템플릿 페이지 지정하기
    template_name='pages/home.html'
    
class AboutPageView(TemplateView):
    # 템플릿 페이지 지정하기
    template_name='pages/about.html'

class ContactPageView(TemplateView):
    # 템플릿 페이지 지정하기
    template_name='pages/contact.html'
    
    
    
    
    
    
    
    
    