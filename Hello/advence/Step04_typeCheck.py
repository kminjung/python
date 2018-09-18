#-*- coding:utf-8 -*-
'''
    변수에 들어있는 데이터의 type 체크
    
    isinstance( 값, type )
    
    메소드는 bool type 을 리턴 합니다.
'''

if __name__ == '__main__':
    # 입력 받기 
    inputData=input('input:')
    
    if isinstance(inputData, int):
        print 'int type!'
    elif isinstance(inputData, long):
        print 'long type!'
    elif isinstance(inputData, float):
        print 'float type!'
    elif isinstance(inputData, str):
        print 'str type!'
    elif isinstance(inputData, dict):
        print 'dict type!'
    elif isinstance(inputData, list):
        print 'list type!'
    else:
        print 'etc type!'
    