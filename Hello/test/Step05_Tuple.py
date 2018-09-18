#-*- coding:utf-8 -*-
'''
    - tuple
    
    1. list type 의  read only 버전 (읽기전용)
    2. 수정, 삭제 불가
    3. list type 보다 처리 속도가 빠르다.
'''

tuple1=(10, 20, 30, 40, 50)

for tmp in tuple1:
    print "tmp:", tmp

# tuple1[0]=999 수정 불가
# del tuplet1[0] 삭제 불가

# 방 1개짜리  tuple 만들때는 주의!
result=(1+1) # input tupe2
result2=(1+1,) # tuple type(2) tuple 라는 것을 알려주기 위해서 , 를 붙인다.
result3=('milk',)# tuple type ('milk')

# 대입할 때 () 생략 가능
result4='milk', 'dari', 'mong'

# 여러개의 변수에 값 한번에 할당하기
a, b, c=10, 20, 30

# 두 변수에 있는 내용을 상호 교환 하려면?
first='girl'
second='boy'

first, second=second, first