#-*- coding:utf-8 -*-
'''
Created on 2018. 9. 18.

@author: lee
'''

if __name__ == '__main__':
    try:
        num1=input('나눌수 입력:')
        num2=input('나누어 지는수 입력:')
        result=num2/float(num1)    
        print '{} 를 {} 로 나눈값은 {} 입니다.'\
            .format(num2, num1, result)
    except ZeroDivisionError, zde: # exception type, 변수 
        print zde
        print '어떤 수를 0 으로 나눌수는 없어요!'
    except ValueError, ve:
        print ve
    except Exception, e: # 위의 두가지를 제외한 모든 예외 
        print e
    else:
        print '예외가 발생 하지 않았습니다.'
    finally:
        print '예외 발생과 상관 없이 실행이 보장되는 블럭'
    
    print '메인 스레드가 종료 됩니다.'
