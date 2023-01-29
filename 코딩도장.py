# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 6.6 연습문제
#소스 코드를 완성하여 정수 세 개를 입력받고 합계가 출력되게 만드세요.

"""
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
"""
#9.3 여러 줄로 된 문자열 사용하기

#s = """Python is a programming language that lets you work quickly 
#and
#integrate systems more effectively."""
#print(s)
#"""

"""
a = '''\'Python\' is a "programming language"
that lets you work quickly
and
integrate systems more effectively.'''
print(a)

10.4 range로 리스트 만들기
a = list(range(5, -10, -2))
print(a)

#심사문제
a = int(input())
b = tuple(range(-10, 10, a))
print(b)



# 11.6 최근 3년간 인구 출력하기
year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]

print(year[-3:])
print(population[-3:])

n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print(n[1::2])

#심사문제
x = input().split()
del x[-5:]
print(tuple(x[0:len(x)]))

#심사문제2
a = input()
b = input()
print(a[1::2]+b[0::2])

#12.4 연습문제
#딕셔너리에 게임 캐릭터 능력치 저장하기

camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}

print(camille['health']
      ,camille['movement_speed'])

#심사문제
a, b = input().split(), input().split()
x = dict(zip(a, b))
print(x)

# 13.6 연습문제 if
x = 5
if x != 10:
    print('ok')

#심사문제
price = int(input())
coupon = input()

if coupon == 'Cash3000':
    print(price - 3000)
elif coupon == 'Cash5000':
    print(price - 5000)

#14.6 연습문제 합격 여부 판단하기
written_test = 75
coding_test = True

if written_test >= 80 and coding_test == True:
    print('합격')
else:
    print('불합격')
 
#심사문제
korean, english, mathmatics, science = map(int, input().split())
score_avg = (korean+english+mathmatics+science)/4
if 0 <= korean <= 100 and 0 <= english <= 100 and 0 <= mathmatics <= 100 and 0 <= science <= 100:
    if score_avg >= 80:
        print('합격')
    else:
       print('불합격')
else:
    print('잘못된 점수')
  
   
#15.3 if,elif,else 사용
x = int(input())

if 11 <= x <= 20:
    print('11~20')
elif 21 <= x <= 30:
    print('20~30')
else:
    print('아무것도 해당하지 않음')

#심사문제
age = int(input())
balance = 9000
 
if 7 <= age <= 12:
     balance = balance - 650    
elif 13 <= age <= 18:
     balance = balance - 1050
elif age >= 19:
     balance = balance - 1250

print(balance)
"""
    