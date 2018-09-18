#-*- coding:utf-8 -*-
'''
    입력한 정보를 문자열로 입력 받기
    
'''

result = raw_input('문자열 입력:')

print 'type:', type(result)
print 'result', result

# str type 을 unicode 로 바꾸기
result2=result.decode('utf-8');

print 'result2 type:', type(result)
print 'result2:', result2