#-*- coding:utf-8 -*-

class Robot:
    # 참조값으로 call 할수 있도록 설정
    def __call__(self):
        print u'참조값으로 call 을 하네??'
    # 객체 차체를 출력할때 출력할 문자열을 리턴 할수 있다.    
    def __str__(self):
        return 'i am robot!'
    
    def walk(self):
        print u'로봇이 걸어요'

if __name__ == '__main__':
    
    # Robot 객체 생성해서 참조값을 r1 에 담기 
    r1=Robot()
    r1.walk()
    # 참조값 자체를 call 하면 __call__() 메소드가 호출된다.  
    r1()
    print r1
