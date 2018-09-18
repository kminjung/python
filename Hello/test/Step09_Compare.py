
#-*- coding:utf-8 -*-
'''
    1. 숫자 비교 
    2. 문자열의 내용비교
    3. 참조값(id) 비교 
    4. 동일한 객체인지 비교 
'''

# 숫자가 같은지 여부는 동등 비교 연산자로 비교 하면 된다.  == , != 
num1=10
num2=20
num3=10

# 문자가 같은지 여부는 동등 비교 연산자로 비교 하면 된다.  == , != 
str1='kim'
str2='lee'
str3='kim'


list1=[10,20]
list2=[10,20]
list3=list1

result1 = list1 == list2 # True
result2 = list2 == list3 # True
result3 = list1 == list3 # True

result4 = id(list1) == id(list2)
result5 = id(list2) == id(list3)
result6 = id(list1) == id(list3)

result7 = list1 is list2
result8 = list2 is list3
result9 = list1 is list3

print u"Step09_Compare.py 가 종료 됩니다."