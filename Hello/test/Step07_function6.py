#-*- coding:utf-8 -*-
'''
    함수의 리턴  type
'''

def test1():
    print 'test1()'

def test2():
    print 'test2()'
    return

r1=test1() #None
r2=test2() #None

def test3():
    print 'test3()'
    return 10

r3=test3() #int type

def test4():
    print 'test4()'
    return {'num':999}

r4=test4() #dict type

def test5():
    print 'test5()'
    names = ['lee', 'kim', 'park']
    return names
r5=test5() #list type

def test6():
    print 'test6()'
    def inner():
        print 'inner()'
    return inner