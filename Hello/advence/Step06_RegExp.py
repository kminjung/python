#-*- coding:utf-8 -*-
'''
    [ 정규 표현식 사용하기 ]
'''
import re

if __name__ == '__main__':
    
    # 검증할 문자열
    msg='Hello, World!'
    # 겁증할 문자열에서 정규 표현식에 매칭되는 문자열이 있으면 
    # Match type 객체가 리턴된다.
    result=re.search('Hello', msg)
    # 없으면 None 이 리턴된다.
    result2=re.search('hello', msg)
    
    if result != None:
        print u'Hello 를 찾았습니다.'
    if result:
        print u'Hello 를 찾았습니다.'
    
    if result2 != None:
        print u'hello 를 찾았습니다.'
    
    if result2:
        print u'hello 를 찾았습니다.'
