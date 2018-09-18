#-*- coding:utf-8 -*-

# MyUtil.py

print u'MyUtil.py 의 __name__ :', __name__

class Messenger:
    def sendMessage(self,msg):
        print msg, u'를 전송합니다.'
        
# main 으로 실행되었을때만 실행할 코드 
if __name__ == '__main__':
    print u'MyUtil.py 가 메인으로 실행되었습니다.'