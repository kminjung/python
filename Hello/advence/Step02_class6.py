#-*- coding:utf-8 -*-

# 데코레이터 역활을 할수 있는 함수(메소드)의 구조 
def MyDeco(func):
    
    def wrapper(*args, **kwargs):
        # 데코레이터가 적용된 함수 수행이전에 할 작업
        func(*args, **kwargs)
        # 데코레이터가 적용된 함수 수행이후에 할 작업
    return wrapper

# 데코레이터를 클래스로 정의할수 있다.

class HelloBye:
    #생성자
    def __init__(self, func): # func 는 데코레이터가 적용된 함수
        # 생성자로 전달되는 함수를 필드에 저장 
        self.func=func
    
    # call 되었을때 할 동작
    def __call__(self, *args, **kwargs):
        # 멤버 메소드 호출 가능!
        self.auth()
        # 데코레이터가 적용된 함수가 수행되기 이전에 작업할 내용   
        print 'hello!'  
        result=self.func(*args, **kwargs)
        # 데코레이터가 적용된 함수가 수행된 이후에 작업할 내용
        print 'bye~'
        return result
    
    def auth(self):
        print u'인증 작업을 해요'
    
    
@HelloBye    
def drive():
    print u'달려요!'
@HelloBye  
def play():
    print u'신나게 놀아요!'

if __name__ == '__main__':
    
    drive()
    play()
