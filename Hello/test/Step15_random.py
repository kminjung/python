#-*- coding:utf-8 -*-
'''
    [ random package 사용하기 ]
'''
import random as ran # import 된 random 의 별칭 부여 

ranNum=ran.random() # 0 이상 1 미만의 무작위 실수 

ranNum2=int(ran.random()*10) # 0 이상 10 미만의 무작위 정수 

ranNum3=int(ran.random()*10)+10 # 10 이상 20 미만의 무작위 정수

ranNum4=int(ran.random()*45)+1 # 1 이상 45 미만의 무작위 정수 

ranNum5=ran.randint(1, 45) # 1 이상 45 미만의 무작위 정수 

# 로또번호

nums=set() # 로또 번호를 담을 set 객체 

# 반복문 돌면서 
while True:
    # 무작위의 로또 번호를 얻어내서 
    lottoNum=ran.randint(1, 45)
    # set 에 추가 한다 
    nums.add(lottoNum)
    # set 에 번호 6 개가 담기면 반복문 탈출 
    if len(nums)==6:
        break

# set 에 있는 숫자를 이용해서 list 객체 얻어내고
lottoList=list(nums)
# 오름 차순 정렬
lottoList.sort()

# list 의 구조 확인 
print lottoList
