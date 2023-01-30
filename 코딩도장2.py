# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 19:58:11 2023

@author: Jeong Hyeonju
"""

#16.1 for/range
"""
for i in range(10):
    print('hello world', i)


for i in reversed(range(10)):
    print(i, end=' ')

fruits = ('apple', 'orange', 'grape')
for letter in reversed('fruits'):
    print(letter, end=' ')


# 16.5 연습문제
x = [49, -17, 25, 102, 8, 62, 21]
for i in x:
    print(i * 10, end=' ')

# 심사문제: 구구단 출력
first = int(input())
for i in range(1, 10):
    print(first,'*',i,'=', i * first)

#17 while
i = 0
while i < 10:
    print('hi', i)
    i += 1

count = int(input('반복 횟수 입력: '))
i = 0
while i < count:
    print('nice', i)
    i += 1
"""

import random
"""
i = 0
while i != 3: #3이 아니면 반복하기
    i = random.randint(1, 10)
    print(i)

dice = [1, 2, 3, 4, 5, 6]
print(random.choice(dice))

#17.5 연습문제: 변수 두 개 다르게 반복
i, j = 2, 5
while i <= 32 or j >= 1:
    print(i, j)
    i *= 2
    j -= 1

#심사문제
price = int(input())
while price >= 1350:
    print(price - 1350)
    price = price - 1350

#18.1 break
i = 0
while True:
    print(i)
    i+= 1
    if i == 10:
        break
    
for i in range(10):
    print(i)
    if 1 == 10:
        break

#18.2 continue
for i in range(100):
    if i % 2 == 0: # i를 2로 나누었을 때 나머지가 0이면 코드 실행을 건너뜀
        continue
    print(i)

i = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

count = int(input('반복 횟수: '))

i = 0
while True:
    print(i)
    i += 1
    if i == count:
        break 
  

for i in range(count + 1):
    if i % 2 == 0:
        continue
    print(i)
 
#18.5 연습문제: 3으로 끝나는 숫자만 출력
i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue
    if i > 73:
        break
    print(i, end=' ')
    i += 1

# 심사문제
# 첫번째 1~200, 두번째 10~200, 첫번째 < 두번째
# 첫번째 정수와 두번째 정수 사이에서 3으로 끝나지 않는 숫자 출력

start, stop = map(int, input().split())

i = start

while True:
    if i > stop:
        break
    if i % 10 == 3:
        i += 1
        continue
    print(i, end=' ')
    i += 1

# 19.계단식으로 별 출력
for i in range(5):
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print('i', i, '\\n', sep='')
    
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()
    
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end=' ')
    print()

for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    
#19.5 연습문제: 역삼각형 모양으로 별 출력
for i in range(5):
    for j in range(5):
        if j>=i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# 심사문제: 산모양 출력
a = int(input())

for i in range(1, a):
    for j in range(a-1, i, -1):
        print(" ")
        
        if i <= j-1:
            print('+', end=' ')
        
    print()
"""
"""
# 20.FizzBuzz
for i in range(1, 101):
    print(i)
    
for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
"""
# 20.5 코드 단축
for i in range(1, 101):
    print('fizz' * (i % 2 == 0) + 'buzz' * (i%3 == 0) or i)
