#-*- coding:utf-8 -*-
'''
    decorator 는 함수의 장식자 이다.
    
    @데코레이터명 
'''

# decorator 로 사용할 함수 정의하기
def helloBye(func):
    #인자로 전달된 func 는 함수의 참조값이다.
    def wrapper():
        print 'hello!'
        func() # 인자로 전달된 함수 호출
        print 'bye~'
    return wrapper # 함수의 참조값 리턴하기 

@helloBye
def f1():
    print u'f1() 수행됨'
@helloBye
def f2():
    print u'f2() 수행됨'
@helloBye
def f3():
    print u'f3() 수행됨'

# 위에서 만든 함수 호출하기 
f1()
f2()
f3()