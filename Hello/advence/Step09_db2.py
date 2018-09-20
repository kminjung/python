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
        
        # 이름, 주소 입력 받기
        inputName=raw_input('이름:').decode('utf-8')
        inputAddr=raw_input('주소:').decode('utf-8')
        
        # 실행할 sql 문
        sql='''
            INSERT INTO member
            (name, addr)
            VALUES(%s, %s)
        '''
        # sql 문 수행하기
        cursor.execute(sql, (inputName, inputAddr))
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
