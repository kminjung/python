#-*- coding:utf-8 -*-
'''
    [ **kwargs ]
    
    - 함수로 전달되는 인자를  dict type 으로 받을 수 있다.
'''

def test1(**kwargs):
    print kwargs
test1(num=1)
test1(num=1, name='milk')
test1(num=2, name='dari', isMan=True)

# *을 붙이면 인자를 여러개 전달할 수 있다. **는 keyward 문자를 전달받을 수 있다. 
#다양한 형태의 호출을 받아줄 수 있는 함수
def test2(*args, **kwargs):
    print "args:", args, "kwargs:", kwargs

test2(10,20)
test2(num=1, name='milk')
test2(30, 40, num=2, name='dari')
