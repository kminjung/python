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
        
        ####
        #수정할 회원의 번호
        inputNum=input('수정할 회원의 번호:')
        inputAddr=raw_input('새로운 주소:').decode('utf-8')
        
        sql='''
            UPDATE member
            SET addr=%s
            WHERE num=%s
        '''
        cursor.execute(sql, (inputAddr, inputNum))
        
        if cursor.rowcount > 0:
            print u'회원 정보를 수정했습니다'
        else:
            print u'회원 정보 수정 실패'
        
        ####   
        # DB 에 실제 반영하기
        conn.commit()
       
    except Exception, e:
        print e
    finally:
        try:
            conn.close()
        except NameError, ne:
            print ne
    
    print u'Step09_db4.py 가 종료 됩니다.'

