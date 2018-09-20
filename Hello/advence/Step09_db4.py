#-*- coding:utf-8 -*-

# Maria DB 연결 객체 
import mysql.connector

# DB 접속 정보를 dict type 에 준비한다.
config={
        'user':'root',       # 계정
        'password':'maria',  # 비밀번호
        'host':'127.0.0.1',  # 접속 ip
        'database':'acorn',  # database 이름
        'port':3306          # 포트번호 (default:3306)
    }

if __name__ == '__main__':
    try:
        #Maria DB 연결 객체 (java : Connection 객체)
        conn=mysql.connector.connect(**config) # dict type 매칭
        # (java : PreparedStatement)
        cursor=conn.cursor()
        
        # 삭제할 회원의 번호 입력받기
        inputNum=input('삭제할 회원의 번호:')
        sql='''
            DELETE FROM member
            WHERE num=%s
            '''
        cursor.execute(sql, (inputNum,))
        #sql 문의 영향을 받은 row 갯수
        updateCount=cursor.rowcount
        if updateCount > 0:
            print u'{} 번 회원 삭제됨'.format(inputNum)
        else:
            print u'{} 번 회원은 존재하지 않습니다.'.format(inputNum)
            
        # DB 에 실제 반영하기
        conn.commit()
      
        print u'회원 정보를 저장했습니다.'
    except Exception, e:
        print e
    finally:
        try:
            conn.close()
        except NameError, ne:
            print ne
    
    print u'Step09_db2.py 가 종료 됩니다.'
