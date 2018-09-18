#-*- coding:utf-8 -*-
'''
    다중 if 문
'''
# 입력한 점수 85 점은 B 입니다.

inputNum=input('점수입력:')

grade=None;

if inputNum >= 90:
    grade='A'
elif inputNum >= 80:
    grade='B'
elif inputNum >= 70:
    grade='C'
elif inputNum >= 60:
    grade='D'
else:
    grade='F'
    
print u'입력한 점수 {} 는 {} 입니다.'.format(inputNum, grade)
