#-*- coding:utf-8 -*-

# test 함수
# def test(num, name, addr):
#     print num, name, addr
#     
# tuple1=(1, u'김구라', u'노량진')
# dict1={'num':2, 'name':u'해골', 'addr':u'행신동'}
# 
# # test 함수 call 하는 방법1
# test(3, u'원숭이', u'동물원')
# # test 함수 call 하는 방법2
# test(*tuple1) # test(1, u'김구라', u'노량진')
# # test 함수 call 하는 방법3
# test(**dict1) # test(num=1,name=u'해골',addr=u'행신동')

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
        # Maria DB 연결 객체 (java : Connection 객체)
        conn=mysql.connector.connect(**config) # dict type 매칭
        # (java : PreparedStatement)
        cursor=conn.cursor()
        # 실행할 query 문 , 여러줄 문자열을 쓰고 싶을 때에는 ''' 을 사용한다.
        sql='''
            SELECT num,name,addr
            FROM member
            ORDER BY num DESC
            '''
        cursor.execute(sql)
        # (java : ResultSet)
        result=cursor.fetchall()
        print result
        '''
            - result 는  tuple 이 저장된  list type 이다.
            - 구조  : [(),(),(), ...]
            - tuple 에는 select 된  row 의 정보가 순서대로 들어있다.
            
        '''
        # 반복문 돌면서 row 의 정보가 들어있는 tuple 을 얻어낸다.
        for tmp in result:
            num=tmp[0]
            name=tmp[1]
            addr=tmp[2]
            print u'번호:{} 이름:{} 주소:{}'\
            .format(num, name, addr) 
        
        
        
    except Exception, e:
        print e
    finally:
        try:
            conn.close()
        except NameError, ne:
            print ne
    
    print u'Step09_db.py 가 종료 됩니다.'
    
'''
    typle 하나하나의 정보는 row 하나하나의 정보
    fetchall - 
'''
