#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse
from memo.models import Memo

# memo/views.py

def hello(request):
    
    return HttpResponse('/memo/hello ok!')

# /memo/list/ 요청 처리 
def list(request):
    # 1. DB 에서 메모 목록을 얻어와서
    memoList=Memo.objects.all().order_by('-id')
    # 2. template html 페이지를 이용해서 메모 목록을 출력한다.
    print memoList
    
    #응답
    return render(request, 'memo/list.html', {'memoList':memoList})
    
    
    
    
    
    
    
    
    
    
    
    
    
    