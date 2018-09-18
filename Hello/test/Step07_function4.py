#-*- coding:utf-8 -*-
'''
    함수를 call 할 때  keyword 인자를 전달할  수도 있다.

'''

def test1(num, name, addr):
    print num, name, addr

test1(1, u'밀크', u'강동구') #순서대로 num, name, addr 에 전달된다.

test1(name=u'milk', num=2, addr=u'성내동' ) # 값들이 keyword를 따라 알아서 찾아간다.

# 함수를 선언할 때 전달되는 인자의  default 값을 저정할 수 있다.
def test2(num=0, name="누굴깡", addr="어딜깡"):
    print num, name, addr

test2()
test2(name=u'무꾸')
test2(num=3, addr=u'우리집')
