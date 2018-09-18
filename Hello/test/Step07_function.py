#-*- coding:utf-8 -*-
'''
    - function type
    
    1. 특정 시점에 일괄 실행할 명령문을 모아 놓을 수 있다.
    2. function 도 참조값으로 관리된다.
    3. 변수에 할당 가능
    4. 함수의 인자로 전달 가능
'''

# test1 이라는 이름의 빈 함수 만들기
def test1():
    pass

test1() #test 함수 호출하기

def test2():
    print "hello~"

test2() #함수를 call

# 함수의 참조값을 변수에 대입
a=test2() # 함수 참조
a()

print u'Step07_function.py 가 종료 됩니다.'