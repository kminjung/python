#-*- coding:utf-8 -*-

# http 요청할수 있는 요청 객체 import
from pip._vendor import requests
import threading

# 스레드 객체를 생성할 클래스 정의하기
class MyThread(threading.Thread):
    #생성자
    def __init__(self, url):
        #부모 생성자에 필요한 값 전달
        threading.Thread.__init__(self)
        #인자로 전달된 url을 필드에 저장
        self.url=url
    # run() 메소드 오버라이딩
    def run(self):
        responseObj=requests.get(self.url)
        print responseObj.text



if __name__ == '__main__':
    print '메인 스레드가 시작됨'
    
    t1=MyThread('http://daum.net')
    
    # 데몬 스레드는 메인 스레드가 종료되면 같이 종료 된다. 
    # t1.daemon=True # 스레드가 시작 되기 전에 설정 
    
    t1.start()
    
    # t1 스레드가 종료 될때 까지 메인 스레드에서 기다리기
    # t1.join()
    
    print '메인 스레드가 종료됨'
