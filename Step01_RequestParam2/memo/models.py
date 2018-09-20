#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

'''
    데이터 Base 에 테이블을 만든다는 느낌으로 클래스를 정의한다.
'''

class Memo(models.Model):
    # 필드정의
    content=models.TextField()
    regdate=models.DateTimeField()
















