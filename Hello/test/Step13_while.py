#-*- coding:utf-8 -*-
'''
    [ while 반복문 ]
'''

count=0

while True: # 외형상 무한 루프 
    print u'반복문 수행중...'
    count += 1 # 카운트 1 증가 시키기 ( count++ 는 없음)
    if count==10: # 특정 조건에서 
        # break 예약어를 이용해서 반복문 탈출 가능 
        break

print u'반복문 탈출후 count:', count

count=0

while count<10:
    print u'반복문 수행중...'
    count += 1
    
print u'반복문 탈출후 count:', count
