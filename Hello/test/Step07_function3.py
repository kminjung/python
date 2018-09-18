#-*- coding:utf-8 -*-
'''
    [ *args ]
    
    - 함수에 여러개의 인자를 동적으로 전달 받을 수 있다.
    
'''

def test1(*arg):
    # args 는 tuple 이다.
    print arg
test1()
test1(10)
test1(10, 20)
test1(10,'milk', True)
 
# 전달받을 준비가 되어있는데 전달하지 않거나 갯수가 많으면 오류가 난다.
