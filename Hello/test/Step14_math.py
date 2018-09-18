#-*- coding:utf-8 -*-
import math # 수학에 관련된 모듈을 제공하는 package

r = input(u'원의 반지름 입력:')

# 원의 넓이 구하기
area = 3.14*r*r

area2 = math.pi*(r**2) #  r**2  는 r 의 2 승

area3 = math.pi*math.pow(r, 2) # math.pow(r, 2) 는 r 의 2 승

print area, area2, area3

num=1234.5678

result1=math.floor(num) # 내림
result2=math.ceil(num) # 올림
resunt3=round(num) # 반올림 
