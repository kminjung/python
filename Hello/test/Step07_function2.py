#-*- coding:utf-8 -*-

'''
    함수에 인자 전달하기
'''

def test1(arg1):
    print "arg1:",arg1

test1("milk")

def test2(a,b):
    print "a:", a, "b:", b

test2('dog', 'cat') # dog 는 a, cat 는 b 에 적용된다.