#-*- coding:utf-8 -*-

names=['kim', 'lee', 'park', 'jo', 'choi']

for item in names:
    print item
    
print '-------'

for i in [0,1,2,3,4]:
    #배열의 i 번째 방 참조 
    tmp=names[i]
    print u'{} : {}'.format(i, tmp)
    
print '-------'

for i in range(5): # 5 는 배열의 방의 갯수 
    #배열의 i 번째 방 참조 
    tmp=names[i]
    print u'{} : {}'.format(i, tmp)
    
print '-------'

for i in range(len(names)): # len(names) 는 배열의 방의 갯수 
    #배열의 i 번째 방 참조 
    tmp=names[i]
    print u'{} : {}'.format(i, tmp)
    
print '-------'

for i in range(len(names)-1, -1):
    tmp=names[i]
    print u'{} : {}'.format(i, tmp)
    
print '-------'  

#1~100까지의 합을 구해서 출력하는 코드를 구성해보세요
tmp=0
for i in range(0,101,1):
    #배열의 i 번째 방 참조 
    tmp=i+tmp
    print u'{} : {}'.format(i, tmp)


