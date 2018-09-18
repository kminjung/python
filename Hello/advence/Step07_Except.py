#-*- coding:utf-8 -*-
'''
    예외처리 문법 학습
'''

if __name__ == '__main__':
    try:
        num1=input('나눌수 입력:')
        num2=input('나누어 지는수 입력:')
        result=num2/num1    
        print '{} 를 {} 로 나눈값은 {} 입니다.'\
            .format(num2, num1, result)
    except ZeroDivisionError, zde: # exception type, 변수 
        print zde
        print '어떤 수를 0 으로 나눌수는 없어요!'
    
    print '메인 스레드가 종료 됩니다.'
    
    
    
    
    
    
    
    
    
    