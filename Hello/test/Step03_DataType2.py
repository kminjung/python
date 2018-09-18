#-*- coding:utf-8 -*-

# list type (추가,수정,삭제 가능한 배열)
nums=[10,20,30,40,50]

names=['milk','mong','dari']

friends=[u'밀크', u'몽이', u'다리']

# tuple type (추가,삭제,수정 불가능한 배열), 수정하지 않을 거면 tuple 배열을 쓰는 것이 좋다.
nums2=(10,20,30,40,50)

names2=('milk','mong','dari')

friends2=(u'밀크',u'몽이',u'다리')

# dict type / object 와 비슷하다. key 값으로 관리된다.
mem1={"num":1, "name":u"밀크", "isMan":False}
mem2={"num2":2, "name":u"다리", "isMan":True}

# function type
def a():
    pass
def b():
    print 'one'
    print 'two'
    print 'three'
b() #b 라는 함수 call 하기
'''
pass 는 function a(){}와 같다. 콜론과 들여쓰기를 이용해서 블럭지정을 한다. 들여쓰기가 끝나면 블럭이 닫힌다.
비워놓고 싶으면 pass 를 쓰면 된다.
'''

# None type
emptyVar=None # java 의 null 이라고 이해 하면 된다.

# set type (집합, 묶음) / 집합의 개념으로 관리하고 싶을 때
set1={10, 20, 30, 10, 20}

print u'Step03_DataType2.py 가 종료 됩니다.'
