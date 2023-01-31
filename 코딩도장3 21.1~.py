# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:14:59 2023

@author: Jeong Hyeonju

# 21.1 사각형 그리기
import turtle as t
t.shape('turtle')

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)

t.mainloop()

# 오각형
for i in range(5): #사각형 = 4번 반복
    t.forward(100)
    t.left(360/5)

# 다각형
n = int(input())
t.shape('turtle')
t.color('red')
t.begin_fill() #현재 펜 색 칠하기
for i in range(n):
    t.fd(100)
    t.rt(360 / n)

n = 60
t.speed('fastest')
for i in range(n):
    t.circle(270)
    t.right(360 / n)

t.speed('fastest')
for i in range(300):
    t.forward(i)
    t.right(91)

# 연습문제 오각별 그리기
t.speed('fastest')
n = 5

for i in range(n):
    t.fd(100)
    t.rt(144)
    t.fd(100)
    t.rt(72)

#22 리스트와 튜플 응용하기
# append 요소 추가
# extend 리스트 연결 확장
# insert 특정 인덱스에 요소 추가

a = [10, 20 ,30]
a.append(500)
print(a, type(a), len(a))

a.append([5, 7])
print(a, len(a))

#a.extend=([200, 1000])
print(a)

a.insert(0, 1)
print(a)

a[1:1] = [500, 600]
print(a)

#삭제
a = [10, 20, 30]
a.pop() #마지막 요소 제거
print(a)

a = [10, 20, 30]
a.pop(1)
print(a)

a=[10,20,30]
del a[0]
print(a)

a = [10, 20, 30]
a.remove(20) #값을 찾아서 지우기
print(a)

a = [10, 20, 30, 20]
a.remove(20) #처음 찾은 20을 제거
print(a)

a = [10, 20, 30, 40, 50]
print(a.index(20)) #20이 있는 인덱스 값

a = [10, 1, 2, 40, 50]
a.reverse() #값들은 반대로 
print(a)

a.sort() #오름차순 정렬
print(a)
a.sort(reverse=True) #내림차순
print(a)

a.clear() #리스트 비우기
print(a)

del a[:] #리스트 비우기
print(a)
"""

#리스트 복사
"""
a = [0, 0, 0, 0, 0]
b = a
print(a, b)
print(a is b)
b[2] = 99
print(a, b)

a = [0, 0, 0, 0]
b = a.copy()
print(a is b,'\n',a == b) #다른 객체기 때문에 false
print(a, b)
b[2] = 99

print(a, b)
"""

#for문으로 요소 출력
"""
a = [22, 11, 33, 44, 55]

for i in a:
    print(i)
    
for index, value in enumerate(a, start=1): #인덱스와 값 함께 추력
    print(index, value)

a = [38, 21, 19, 10, 34]
i = 0
while i < len(a):
    print(a[i])
    i += 1
"""
a = [38, 21, 19, 10, 34]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i
        
print(smallest, end=' ')

largest = a[0]
for i in a:
    if i > largest:
        largest = i
print(largest)

print(min(a), max(a))

x = 0
for i in a:
    x += i
    
print(x, sum(a))

   








