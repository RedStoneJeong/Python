# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 6.6 연습문제
#소스 코드를 완성하여 정수 세 개를 입력받고 합계가 출력되게 만드세요.

a, b, c = map(int, input().split())
print(a + b + c)

# 7.4 연습문제
#날짜와 시간이 출력되게 만들기

year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59

print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')

# 8.4 연습문제
# 합격여부 출력
korean = 92
english = 47
mathmatics = 86
science = 81

print(korean >= 50 and english >= 47 and mathmatics >= 86 and science >= 81)
ko, en, ma, sc = map(int, input().split())
print(ko >= 90 and en > 80 and ma > 85 and sc >=80)





