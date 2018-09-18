#-*- coding:utf-8 -*-
'''
    [ 반복문 for ]
'''

for item in [10, 20, 30]:#list type
    print item
'''
    range( start, end, step)
    
    range(10) end=10, start=0, step=1
    range(20) end=20, start=0, step=1
    range(1, 10) start=1, end=10, step=1
    range(0,10,2) start=0, end=10, step=2
'''    
result1=range(10) #0이상 10미만의 정수들을 리턴한다.
result2=range(1,10) #1이상 10미만의 정수들을 리턴한다.
result3=range(1,20)
result4=range(10,20)
result5=range(0, 10, 2)
result6=range(0, 20, 3)

print result1
print result2
print result3
print result4
print result5
print result6

